from datetime import datetime
from uuid import uuid4

from serializer.constants.constants import UUID_DATE_FORMAT
from serializer.Serializable import Serializable


class Song(Serializable):

    def __init__(self, title: str, artist: str):
        if not issubclass(Song, Serializable):
            raise NotImplementedError
        super().__init__()
        self.song_id: str = datetime.now().strftime(UUID_DATE_FORMAT) + str(uuid4())
        self.title: str = title
        self.artist: str = artist
