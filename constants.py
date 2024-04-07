from enum import Enum
from typing import Literal

SONG = 'song'
TITLE = 'title'
ARTIST = 'artist'


class FormatEnum(Enum):
    JSON: str = 'JSON'
    XML: str = 'XML'


format_type: type[FormatEnum] = Literal[
    FormatEnum.JSON, FormatEnum.XML
]

UUID_DATE_FORMAT = '%Y%m%d-%H%M%S-'
