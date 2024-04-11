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

{"id": "20240411-160311-f4524550-1b65-4b4e-8c23-bc6d081b5af7", "title": "You are more", "artist": "Tenth Avenue North"}
<song_id id="20240411-160311-f4524550-1b65-4b4e-8c23-bc6d081b5af7"><title>You are more</title><artist>Tenth Avenue North</artist></song_id>
artist: Tenth Avenue North
id: 20240411-160311-f4524550-1b65-4b4e-8c23-bc6d081b5af7
title: You are more
"""

if __name__ == "__main__":
    proceed()
