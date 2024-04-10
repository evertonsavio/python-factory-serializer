from typing import Generic, TypeVar
from serializer_module.models.common.SerializableInterface import SerializableInterface
from serializer_module.models.serializables.SerializableObject import SerializableObject
from serializer_module.serializers.AbstractSerializer import AbstractSerializer

T = TypeVar("T", bound=SerializableObject)


class Serializable(Generic[T], SerializableInterface):

    def __init__(self, t: T):
        if not issubclass(Serializable, SerializableInterface):
            raise NotImplementedError
        if not issubclass(type(t), SerializableObject):
            raise NotImplementedError
        self.t: T = t

    def serialize(self, serializer: AbstractSerializer):
        for index, (x, y) in enumerate(vars(self.t).items()):
            if index == 0:
                serializer.start_object(x, y)
            else:
                serializer.add_property(x, y)
