from abc import ABCMeta, abstractmethod
from serializer.constants.registers import FormatType
from serializer.serializables.AbstractSerializable import AbstractSerializable
from serializer.serializers.Serializer import Serializer


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
    def _register_format(self, file_format: FormatType, creator: type[Serializer]):
        raise NotImplementedError

    @abstractmethod
    def _get_serializer(self, file_format: FormatType):
        raise NotImplementedError

    @abstractmethod
    def make(self, serializable: AbstractSerializable, file_format: FormatType) -> str:
        raise NotImplementedError
