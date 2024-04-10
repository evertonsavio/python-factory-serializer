from abc import abstractmethod, ABCMeta
from typing import TypeVar
from serializer.serializers.Serializer import Serializer

K = TypeVar("K", bound=Serializer)


class AbstractSerializable(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, 'make_serializable') and
                callable(__subclass.make_serializable))

    @abstractmethod
    def make_serializable(self, serializer: K):
        raise NotImplementedError
