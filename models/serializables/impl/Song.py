from datetime import datetime
from uuid import uuid4

from constants.constants import UUID_DATE_FORMAT
from models.serializables.SerializableObject import SerializableObject


class Song(SerializableObject):

    def __init__(self, title: str, artist: str):
        if not issubclass(Song, SerializableObject):
            raise NotImplementedError
        super().__init__()
        self.song_id: str = datetime.now().strftime(UUID_DATE_FORMAT) + str(uuid4())
        self.title: str = title
        self.artist: str = artist
