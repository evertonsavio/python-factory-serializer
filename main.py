from serializer.constants.registers import FormatType
from project.models.Song import Song


def proceed():

    song = Song('You are more', 'Tenth Avenue North')

    json: str = song.serialize(FormatType.JSON)
    print(json)

    xml: str = song.serialize(FormatType.XML)
    print(xml)


"""
Output:

{"id": "20240411-154543-41473bee-22e7-44fd-992a-f08c2d2d8454", "title": "You are more", "artist": "Tenth Avenue North"}
<song_id id="20240411-154543-41473bee-22e7-44fd-992a-f08c2d2d8454"><title>You are more</title><artist>Tenth Avenue North</artist></song_id>
"""

if __name__ == "__main__":
    proceed()
