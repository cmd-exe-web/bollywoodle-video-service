import os


# AWS Configurations
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

# Mongodb Configurations
MONGO_URI = "mongodb+srv://admin123:XOC8bvVpsXwlUqu4@cluster0.vipj8mz.mongodb.net/bollywoodle?retryWrites=true&w=majority"
DATABASE_NAME = "bollywoodle"
COLLECTION_NAME = "videos"
