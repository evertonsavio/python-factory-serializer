from enum import Enum
from serializer_module.serializers.AbstractSerializer import AbstractSerializer
from serializer_module.serializers.impl.JsonSerializer import JsonSerializer
from serializer_module.serializers.impl.XmlSerializer import XmlSerializer
from serializer_module.serializers.impl.YamlSerializer import YamlSerializer


class FormatType(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'
    YAML: str = "YAML"


serializer_registers: dict[FormatType, type[AbstractSerializer]] = {
    FormatType.JSON: JsonSerializer,
    FormatType.XML: XmlSerializer,
    FormatType.YAML: YamlSerializer
}
