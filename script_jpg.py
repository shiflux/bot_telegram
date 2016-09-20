import glob
import os
import json

list = glob.glob("images/*.jpg")
new_list = []
for l in list:
    name = os.path.basename(l)
    image_path = "http://31.14.139.243/"+l
    if os.path.isfile("thumbnails/"+os.path.basename(l)):
        thumbnail = "http://31.14.139.243/thumbnails/"+os.path.basename(l)
    else:
        thumbnail = image_path
    new_list.append({"name": name,"link": image_path,"thumbnail": thumbnail})

with open('images.json', 'w') as outfile:
    json.dump(new_list, outfile, indent=4)