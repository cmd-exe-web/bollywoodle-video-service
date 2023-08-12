from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from .controllers.controller import (
    ListObjectNamesResource,
    GenerateClip,
    S3Resource,
    MongoDbResource,
)


app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

api.add_resource(ListObjectNamesResource, "/list-object-names")
api.add_resource(GenerateClip, "/generate-clip")
api.add_resource(S3Resource, "/upload/<string:file_name>")
api.add_resource(MongoDbResource, "/mongodb/<string:document_name>")

if __name__ == "__main__":
    app.run(debug=True)
