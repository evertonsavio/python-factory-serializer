from abc import ABCMeta, abstractmethod
from serializer_module.constants.registers import FormatType
from serializer_module.models.common.SerializableInterface import SerializableInterface
from serializer_module.serializers.AbstractSerializer import AbstractSerializer


class AbstractFactory(metaclass=ABCMeta):

    __abstractmethods__ = None

    @classmethod
    def __subclasshook__(cls, subclass):
        subclass_dict = subclass.__mro__[0].__dict__
        cls_dict = cls.__mro__[0].__dict__
        cls_abstract_methods = cls.__abstractmethods__

        for method_name, method in cls_dict.items():
            if method_name in cls_abstract_methods and hasattr(method, '__annotations__'):
                if method_name not in subclass_dict or \
                        subclass_dict[method_name].__annotations__ != cls_dict[method_name].__annotations__:
                    return False
        return True

    @abstractmethod
    def _register_format(self, file_format: FormatType, creator: type[AbstractSerializer]):
        raise NotImplementedError

    @abstractmethod
    def _get_serializer(self, file_format: FormatType):
        raise NotImplementedError

    @abstractmethod
    def serialize(self, serializable: SerializableInterface, file_format: FormatType) -> str:
        raise NotImplementedError
