from abc import ABC, abstractmethod


class AbstractSerializer(ABC):

    @abstractmethod
    def start_object(self, object_name: str, object_id: str):
        pass

    @abstractmethod
    def add_property(self, name: str, value: str):
        pass

    @abstractmethod
    def to_str(self):
        pass
