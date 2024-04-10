import yaml

from serializer_module.serializers.impl.JsonSerializer import JsonSerializer


class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)
