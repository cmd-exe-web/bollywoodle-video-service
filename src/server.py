from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from src.controllers.controller import (
    ListObjectNamesResource,
    GenerateClip,
    S3Resource,
    MongoDbResource,
    SignupApi,
)
from src.config import MONGO_URI, DATABASE_NAME
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
app.config["MONGODB_SETTINGS"] = {
    "db": DATABASE_NAME,
    "host": MONGO_URI,
}
db = MongoEngine(app)


api.add_resource(ListObjectNamesResource, "/list-object-names")
api.add_resource(GenerateClip, "/generate-clip")
api.add_resource(S3Resource, "/upload/<string:file_name>")
api.add_resource(MongoDbResource, "/mongodb/<string:document_name>")
api.add_resource(SignupApi, "/auth")


if __name__ == "__main__":
    app.run(debug=True)
