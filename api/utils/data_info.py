import json
import os

def get(dir):
    print(os.getcwd())
    dir = os.getcwd()+"/data/"+dir
    file = open(dir, "r", encoding="utf-8")
    data = json.load(file)
    return data