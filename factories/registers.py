from enum import Enum
from serializers.AbstractSerializer import AbstractSerializer
from serializers.impl.JsonSerializer import JsonSerializer
from serializers.impl.XmlSerializer import XmlSerializer
from serializers.impl.YamlSerializer import YamlSerializer


class FormatType(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'
    YAML: str = "YAML"


serializer_registers: dict[FormatType, type[AbstractSerializer]] = {
    FormatType.JSON: JsonSerializer,
    FormatType.XML: XmlSerializer,
    FormatType.YAML: YamlSerializer
}
