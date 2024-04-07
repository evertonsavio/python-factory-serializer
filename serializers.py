import json
from xml.etree.ElementTree import Element, SubElement, tostring
# pip install PyYAML
# import yaml


class BaseSerializer:

    def __init__(self):
        pass

    def start_object(self, object_name: str, object_id: str):
        pass

    def add_property(self, name: str, value: str):
        pass

    def to_str(self):
        pass


class SerializerInterface:

    def __init__(self):
        pass

    def serialize(self, serializer: BaseSerializer):
        pass


class JsonSerializer(BaseSerializer):

    def __init__(self):
        super().__init__()
        self._current_object = None

    def start_object(self, object_name: str, object_id: str):
        self._current_object: dict[str, str] = {
            'id': object_id
        }

    def add_property(self, name: str, value: str):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(BaseSerializer):

    def __init__(self):
        super().__init__()
        self._element = None

    def start_object(self, object_name: str, object_id: str):
        self._element = Element(object_name, attrib={'id': object_id})

    def add_property(self, name: str, value: str):
        prop = SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return tostring(self._element, encoding='unicode')


class YamlSerializer(JsonSerializer):
    def to_str(self):
        return "not implemented yet"
        # return yaml.dump(self._current_object)
