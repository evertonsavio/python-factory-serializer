from serializer.constants.registers import FormatType
from serializer.factories.impl.SerializerFactory import SerializerFactory
from serializer.serializables.impl.SerializableObject import SerializableObject


class Serializable:

    def serialize(self, format_type: FormatType) -> str:
        return SerializerFactory().make(SerializableObject(self), format_type)
