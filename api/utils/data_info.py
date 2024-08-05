import json

def get(dir):
    dir = "/data/"+dir
    file = open(dir, "r")
    data = json.load(file)
    return data