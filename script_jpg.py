import glob
import os
import json
from sett import settings


img_list = glob.glob("images/*.jpg")
new_list = []
for l in img_list:
    name = os.path.basename(l)
    image_path = settings.server+l
    if os.path.isfile("thumbnails/"+os.path.basename(l)):
        thumbnail = settings.server+"thumbnails/"+os.path.basename(l)
    else:
        thumbnail = image_path
    new_list.append({"name": name,"link": image_path,"thumbnail": thumbnail})

with open('images.json', 'w') as outfile:
    json.dump(new_list, outfile, indent=4)