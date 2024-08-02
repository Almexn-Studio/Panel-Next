from pymongo import MongoClient
import config

mongodb_url = config.get('database','url')
client = MongoClient()