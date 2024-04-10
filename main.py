from serializer.constants.registers import FormatType
from project.models.Song import Song


def proceed():

    song = Song('You are more', 'Tenth Avenue North')

    json: str = song.serialize(FormatType.JSON)
    print(json)

    xml: str = song.serialize(FormatType.XML)
    print(xml)

    yaml: str = song.serialize(FormatType.YAML)
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
