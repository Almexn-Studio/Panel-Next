from pymongo import MongoClient
import config

mongodb_url = "mongodb://"
mongodb_url += config.get('database','username')
mongodb_url += ":"+config.get('database','password')

client = MongoClient(mongodb_url)
db = client["runoobdb"]

def add_document(collections:str, document:list):
    col = db[collections]
    return col.insert_many(document)