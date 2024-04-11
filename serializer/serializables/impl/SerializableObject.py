from typing import Generic, TypeVar
from serializer.serializables.AbstractSerializable import AbstractSerializable
from serializer.serializers.Serializer import Serializer

T = TypeVar("T")


class SerializableObject(Generic[T], AbstractSerializable):

    def __init__(self, t: T):
        if not issubclass(SerializableObject, AbstractSerializable):
            raise NotImplementedError

        self.t: T = t

    def make_serializable(self, serializer: Serializer):
        for index, (x, y) in enumerate(vars(self.t).items()):
            if index == 0:
                serializer.start_object(x, y)
            else:
                serializer.add_property(x, y)
