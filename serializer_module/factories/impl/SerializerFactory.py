from serializer_module.constants.registers import FormatType, serializer_registers
from serializer_module.factories.AbstractFactory import AbstractFactory
from serializer_module.models.common.SerializableInterface import SerializableInterface
from serializer_module.serializers.AbstractSerializer import AbstractSerializer


class SerializerFactory:

    __slots__ = ['__creators']

    def __init__(self):
        if not issubclass(SerializerFactory, AbstractFactory):
            raise NotImplementedError
        self.__creators: dict[FormatType, type[AbstractSerializer]] = {}
        for x, y in serializer_registers.items():
            self._register_format(x, y)

    def _register_format(self, file_format: FormatType, creator: type[AbstractSerializer]):
        self.__creators[file_format] = creator

    def _get_serializer(self, file_format: FormatType):
        creator = self.__creators.get(file_format)
        if not creator:
            raise ValueError(file_format)
        return creator()

    def serialize(self, serializable: SerializableInterface, file_format: FormatType) -> str:
        serializer = self._get_serializer(file_format)
        serializable.serialize(serializer)
        return serializer.to_str()
