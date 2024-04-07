from datetime import datetime
from uuid import uuid4

from constants import *
from serializers import SerializerInterface, JsonSerializer, XmlSerializer


class Song(SerializerInterface):

    __slots__ = ['__song_id', '__title', '__artist']

    def __init__(self, title: str, artist: str):
        super().__init__()
        self.__song_id: str = datetime.now().strftime(UUID_DATE_FORMAT) + str(uuid4())
        self.__title: str = title
        self.__artist: str = artist

    def serialize(self, serializer: JsonSerializer | XmlSerializer):
        serializer.start_object(SONG, self.__song_id)
        serializer.add_property(TITLE, self.__title)
        serializer.add_property(ARTIST, self.__artist)
