import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True

    # Mongodb Configurations
    MONGODB_SETTINGS = {"db": "bollywoodle", "host": os.environ.get("MONGO_URI")}
    COLLECTION_NAME = "videos"