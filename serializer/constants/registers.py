from enum import Enum
from serializer.serializers.Serializer import Serializer
from serializer.serializers.impl.JsonSerializer import JsonSerializer
from serializer.serializers.impl.XmlSerializer import XmlSerializer
from serializer.serializers.impl.YamlSerializer import YamlSerializer


class FormatType(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'
    YAML: str = "YAML"


serializer_registers: dict[FormatType, type[Serializer]] = {
    FormatType.JSON: JsonSerializer,
    FormatType.XML: XmlSerializer,
    FormatType.YAML: YamlSerializer
}
