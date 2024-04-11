from serializer.constants.registers import FormatType, serializer_registers
from serializer.factories.AbstractFactory import AbstractFactory
from serializer.serializables.AbstractSerializable import AbstractSerializable
from serializer.serializers.Serializer import Serializer


class SerializerFactory:

    __slots__ = ['__serializers']

    def __init__(self):
        if not issubclass(SerializerFactory, AbstractFactory):
            raise NotImplementedError

        self.__serializers: dict[FormatType, type[Serializer]] = {}
        for x, y in serializer_registers.items():
            self.__serializers[x] = y

    def make(self, serializable: AbstractSerializable, file_format: FormatType) -> str:
        serializer = self.__serializers.get(file_format)()
        if not serializer:
            raise ValueError(file_format)

        serializable.make_serializable(serializer)
        return serializer.to_str()
