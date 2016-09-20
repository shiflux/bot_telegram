import os
import json

images = []
sounds = []
if os.path.isfile("images.json"):
    with open("images.json") as infile:
        images = json.load(infile)

if os.path.isfile("sounds.json"):
    with open("sounds.json") as infile:
        sounds = json.load(infile)

with open('bot_setup.json', 'w') as outfile:
    json.dump({"images":images, "sounds":sounds}, outfile, indent=4)