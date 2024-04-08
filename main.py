from factories.factory import ObjectSerializer
from factories.registers import FormatType
from models.common import SerializableInterface
from models.songs.impl.Song import Song


def proceed():

    song: Song = Song('You are more', 'Tenth Avenue North')
    print(issubclass(Song, SerializableInterface.SerializableInterface))

    serializer = ObjectSerializer()

    json: str = serializer.serialize(song, FormatType.JSON)
    print(json)

    xml: str = serializer.serialize(song, FormatType.XML)
    print(xml)

    yaml: str = serializer.serialize(song, FormatType.YAML)
    print(yaml)


"""
Output:

True
{"id": "20240408-190136-3935475d-328e-46bf-9f29-2274df27a431", "title": "You are more", "artist": "Tenth Avenue North"}
<song id="20240408-190136-3935475d-328e-46bf-9f29-2274df27a431"><title>You are more</title><artist>Tenth Avenue North</artist></song>
artist: Tenth Avenue North
id: 20240408-190136-3935475d-328e-46bf-9f29-2274df27a431
title: You are more
"""

if __name__ == "__main__":
    proceed()
