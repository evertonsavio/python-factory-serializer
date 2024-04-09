import abc

from typing import TypeVar

from serializers.AbstractSerializer import AbstractSerializer

K = TypeVar("K", bound=AbstractSerializer)


class SerializableInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, 'serialize') and
                callable(__subclass.serialize))

    @abc.abstractmethod
    def serialize(self, serializer: K):
        raise NotImplementedError

