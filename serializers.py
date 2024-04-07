import json
from xml.etree.ElementTree import Element, SubElement, tostring


class JsonSerializer:

    def __init__(self):
        self._current_object = None

    def start_object(self, object_name: str, object_id: str):
        self._current_object: dict[str, str] = {
            'id': object_id
        }

    def add_property(self, name: str, value: str):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:

    def __init__(self):
        self._element = None

    def start_object(self, object_name: str, object_id: str):
        self._element = Element(object_name, attrib={'id': object_id})

    def add_property(self, name: str, value: str):
        prop = SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return tostring(self._element, encoding='unicode')


class SerializerInterface:

    def __init__(self):
        pass

    def serialize(self, serializer: JsonSerializer | XmlSerializer):
        pass
