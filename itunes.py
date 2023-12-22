import json
import requests
import sys

my_list = []
if len(sys.argv) != 2:
    sys.exit()
req = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
req1= req.json()
for n in req1['results']:
    print(f'{n["trackName"]} is the song name and {n["artistName"]} is the artist .').strip
