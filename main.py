from factory import ObjectSerializer
from songs import *

song = Song('You are more', 'Tenth Avenue North')

json = ObjectSerializer.serialize(song, FormatEnum.JSON)
print(json)

xml = ObjectSerializer.serialize(song, FormatEnum.XML)
print(xml)

"""
Output:

{"id": "20240407-182440-1c05ff87-2632-4fb5-a126-fb8eda32388b", "title": "You are more", "artist": "Tenth Avenue North"}
<song id="20240407-182440-1c05ff87-2632-4fb5-a126-fb8eda32388b"><title>You are more</title><artist>Tenth Avenue North</artist></song>
"""