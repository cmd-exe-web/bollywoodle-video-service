from flask import Flask
from flask_restful import Api
from .controllers.controller import (
    ListObjectNamesResource,
    VideoClipResource,
    S3Resource,
)


app = Flask(__name__)
api = Api(app)


api.add_resource(ListObjectNamesResource, "/list-object-names")
api.add_resource(VideoClipResource, "/generate-clip")
api.add_resource(S3Resource, "/upload/<string:file_name>")

if __name__ == "__main__":
    app.run(debug=True)
