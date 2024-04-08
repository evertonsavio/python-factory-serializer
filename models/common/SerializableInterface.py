import abc

from serializers.AbstractSerializer import AbstractSerializer


class SerializableInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, 'serialize') and
                callable(__subclass.serialize))

    @abc.abstractmethod
    def serialize(self, serializer: AbstractSerializer):
        raise NotImplementedError
