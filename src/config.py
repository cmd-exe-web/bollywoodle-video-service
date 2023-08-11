import os

# AWS Configurations
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

# Mongodb Configurations
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "bollywoodle"
COLLECTION_NAME = "videos"
