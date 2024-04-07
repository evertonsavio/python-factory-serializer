from constants import FormatType
from serializers import JsonSerializer, XmlSerializer, BaseSerializer, YamlSerializer

serializer_registers: dict[FormatType, type[BaseSerializer]] = {
    FormatType.JSON: JsonSerializer,
    FormatType.XML: XmlSerializer,
    FormatType.YAML: YamlSerializer
}
