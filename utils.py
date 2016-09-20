import json
import urllib2
def load_json(path):
    return json.load(urllib2.urlopen(path))

def get_from_json(path, items):
    return load_json(path)[items]