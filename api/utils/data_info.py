import json

def get(dir):
    dir = "/data/"+dir
    data = json.load(dir)
    return data