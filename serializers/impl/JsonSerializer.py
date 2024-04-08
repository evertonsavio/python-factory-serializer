from serializers.AbstractSerializer import AbstractSerializer
import json


class JsonSerializer(AbstractSerializer):

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
