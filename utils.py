import pymongo
import os


def get_db():
    client = pymongo.MongoClient(os.environ.get("MONGO_URL"))
    return client.itba
