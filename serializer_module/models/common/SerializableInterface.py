from abc import abstractmethod, ABCMeta
from typing import TypeVar
from serializer_module.serializers.AbstractSerializer import AbstractSerializer

K = TypeVar("K", bound=AbstractSerializer)


class SerializableInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, 'serialize') and
                callable(__subclass.serialize))

    @abstractmethod
    def serialize(self, serializer: K):
        raise NotImplementedError
