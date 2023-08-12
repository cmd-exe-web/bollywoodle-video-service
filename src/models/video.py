from pymongo import MongoClient
from ..config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


class Video:
    @staticmethod
    def create_document(document_name):
        collection.insert_one({"name": document_name})
