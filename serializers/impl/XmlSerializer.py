from serializers.AbstractSerializer import AbstractSerializer
from xml.etree.ElementTree import Element, SubElement, tostring


class XmlSerializer(AbstractSerializer):

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
