from enum import Enum
from serializer.serializers.Serializer import Serializer
from serializer.serializers.impl.JsonSerializer import JsonSerializer
from serializer.serializers.impl.XmlSerializer import XmlSerializer


class FormatType(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'


serializer_registers: dict[FormatType, type[Serializer]] = {
    FormatType.JSON: JsonSerializer,
    FormatType.XML: XmlSerializer,
}
