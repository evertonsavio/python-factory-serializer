from factories.factory import ObjectSerializer
from factories.registers import FormatType
from models.common.impl.Serializable import Serializable

from models.serializables.impl.Song import Song


def proceed():

    song = Song('You are more', 'Tenth Avenue North')
    serializable_song = Serializable[Song](song)

    serializer = ObjectSerializer()

    json: str = serializer.serialize(serializable_song, FormatType.JSON)
    print(json)

    xml: str = serializer.serialize(serializable_song, FormatType.XML)
    print(xml)

    yaml: str = serializer.serialize(serializable_song, FormatType.YAML)
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
