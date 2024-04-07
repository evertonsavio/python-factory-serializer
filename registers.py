from constants import FormatType, format_type
from serializers import JsonSerializer, XmlSerializer, BaseSerializer, YamlSerializer

serializer_registers: dict[format_type, type[BaseSerializer]] = {
    FormatType.JSON: JsonSerializer,
    FormatType.XML: XmlSerializer,
    FormatType.YAML: YamlSerializer
}
