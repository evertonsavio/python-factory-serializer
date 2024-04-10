from serializer.constants.registers import FormatType, serializer_registers
from serializer.factories.AbstractFactory import AbstractFactory
from serializer.serializables.AbstractSerializable import AbstractSerializable
from serializer.serializers.Serializer import Serializer


class SerializerFactory:

    __slots__ = ['__creators']

    def __init__(self):
        if not issubclass(SerializerFactory, AbstractFactory):
            raise NotImplementedError
        self.__creators: dict[FormatType, type[Serializer]] = {}
        for x, y in serializer_registers.items():
            self._register_format(x, y)

    def _register_format(self, file_format: FormatType, creator: type[Serializer]):
        self.__creators[file_format] = creator

    def _get_serializer(self, file_format: FormatType):
        creator = self.__creators.get(file_format)
        if not creator:
            raise ValueError(file_format)
        return creator()

    def make(self, serializable: AbstractSerializable, file_format: FormatType) -> str:
        serializer = self._get_serializer(file_format)
        serializable.make_serializable(serializer)
        return serializer.to_str()
