import os
from pymongo import MongoClient

# AWS Configurations
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

# Mongodb Configurations
MONGO_URI = "mongodb+srv://admin123:XOC8bvVpsXwlUqu4@cluster0.vipj8mz.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "bollywoodle"
COLLECTION_NAME = "videos"


client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
