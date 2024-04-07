from constants import FormatType
from registers import serializer_registers
from serializers import BaseSerializer, SerializerInterface


class SerializerFactory:

    __slots__ = ['__creators']

    def __init__(self):
        self.__creators: dict[FormatType, type[BaseSerializer]] = {}

    def register_format(self, file_format: FormatType, creator: type[BaseSerializer]):
        self.__creators[file_format] = creator

    def get_serializer(self, file_format: FormatType):
        creator = self.__creators.get(file_format)
        if not creator:
            raise ValueError(file_format)
        return creator()


class ObjectSerializer:

    __slots__ = ['__factory']

    def __init__(self):
        self.__factory = SerializerFactory()
        for x, y in serializer_registers.items():
            self.__factory.register_format(x, y)

    def serialize(self, serializable: SerializerInterface, file_format: FormatType) -> str:
        serializer = self.__factory.get_serializer(file_format)
        serializable.serialize(serializer)
        return serializer.to_str()
