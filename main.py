from factory import ObjectSerializer
from songs import *

song: Song = Song('You are more', 'Tenth Avenue North')

json: str = ObjectSerializer.serialize(song, FormatType.JSON)
print(json)

xml: str = ObjectSerializer.serialize(song, FormatType.XML)
print(xml)

"""
Output:

{"id": "20240407-182440-1c05ff87-2632-4fb5-a126-fb8eda32388b", "title": "You are more", "artist": "Tenth Avenue North"}
<song id="20240407-182440-1c05ff87-2632-4fb5-a126-fb8eda32388b"><title>You are more</title><artist>Tenth Avenue North</artist></song>
"""