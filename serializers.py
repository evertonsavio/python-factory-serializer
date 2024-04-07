import json
from xml.etree.ElementTree import Element, SubElement, tostring


class SerializerInterface:

    def __init__(self):
        pass

    def start_object(self, object_name, object_id):
        print("Only interface, needs to implemented on child")

    def add_property(self, name, value):
        print("Only interface, needs to implemented on child")


class JsonSerializer(SerializerInterface):

    def __init__(self):
        super().__init__()
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(SerializerInterface):

    def __init__(self):
        super().__init__()
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return tostring(self._element, encoding='unicode')
