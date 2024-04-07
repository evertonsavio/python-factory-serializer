from enum import Enum

SONG: str = 'song'
TITLE: str = 'title'
ARTIST: str = 'artist'


class FormatType(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'
    YAML: str = "YAML"


UUID_DATE_FORMAT: str = '%Y%m%d-%H%M%S-'
