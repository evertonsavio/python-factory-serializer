from abc import ABC

import yaml

from serializers.impl.JsonSerializer import JsonSerializer


class YamlSerializer(JsonSerializer, ABC):
    def to_str(self):
        return yaml.dump(self._current_object)
