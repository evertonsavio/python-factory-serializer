from enum import Enum
from typing import Literal

SONG: str = 'song'
TITLE: str = 'title'
ARTIST: str = 'artist'


class FormatType(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'


format_type: type[FormatType] = Literal[
    FormatType.JSON, FormatType.XML
]

UUID_DATE_FORMAT: str = '%Y%m%d-%H%M%S-'
