from constants import format_type, FormatEnum
from serializers import JsonSerializer, XmlSerializer


class SerializerFactory:
    @staticmethod
    def get_serializer(file_format: format_type) -> JsonSerializer | XmlSerializer:
        if file_format == FormatEnum.JSON:
            return JsonSerializer()
        elif file_format == FormatEnum.XML:
            return XmlSerializer()
        else:
            raise ValueError(file_format)


class ObjectSerializer:
    @staticmethod
    def serialize(serializable, file_format: format_type) -> str:
        serializer = SerializerFactory.get_serializer(file_format)
        serializable.serialize(serializer)
        return serializer.to_str()
