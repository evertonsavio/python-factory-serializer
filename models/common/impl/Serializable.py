from typing import Generic, TypeVar

from models.common.SerializableInterface import SerializableInterface
from models.serializables.SerializableObject import SerializableObject
from serializers.AbstractSerializer import AbstractSerializer

T = TypeVar("T", bound=SerializableObject)


class Serializable(Generic[T]):

    def __init__(self, t: T):
        if not issubclass(Serializable, SerializableInterface):
            raise NotImplementedError
        self.t: T = t

    def serialize(self, serializer: AbstractSerializer):
        for index, (x, y) in enumerate(vars(self.t).items()):
            if index == 0:
                serializer.start_object(x, y)
            else:
                serializer.add_property(x, y)
