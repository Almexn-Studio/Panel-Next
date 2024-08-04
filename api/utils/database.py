from pymongo import MongoClient
import config

mongodb_url = "mongodb://"
mongodb_url += config.get('database','username')
mongodb_url += ":"+config.get('database','password')
mongodb_url += "@"+config.get('database','ip')+"/"

client = MongoClient(mongodb_url)
db = client["runoobdb"]

def add_document(collections:str, document:list):
    col = db[collections]
    return col.insert_many(document)

def get_document(collections:str, query:dict):
    col = db[collections]
    return col.find(query)

def update_document(collections:str, query:dict, new_data:dict):
    col = db[collections]
    return col.update_many(query, new_data)

def delete_document(collections:str, query:dict):
    col = db[collections]
    return col.delete_many(query)