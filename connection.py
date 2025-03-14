from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://karolimartinez:1030080400@clusterisa.z8b3g.mongodb.net/?retryWrites=true&w=majority&appName=Clusterisa"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection
