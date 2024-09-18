import os

from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "mongodb://host.docker.internal:27017/mydatabase")
conn = MongoClient(mongo_uri)