from factory import ObjectSerializer
from songs import *

song: Song = Song('You are more', 'Tenth Avenue North')
serializer = ObjectSerializer()

json: str = serializer.serialize(song, FormatType.JSON)
print(json)

xml: str = serializer.serialize(song, FormatType.XML)
print(xml)

yaml: str = serializer.serialize(song, FormatType.YAML)
print(yaml)

"""
Output:

{"id": "20240407-201737-ccdfd304-2d6c-4007-ab96-a2592d914525", "title": "You are more", "artist": "Tenth Avenue North"}
<song id="20240407-201737-ccdfd304-2d6c-4007-ab96-a2592d914525"><title>You are more</title><artist>Tenth Avenue North</artist></song>
not implemented yet
"""