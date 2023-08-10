from flask import Flask
from flask_restful import Api
from .controllers.controller import ListObjectNamesResource


app = Flask(__name__)
api = Api(app)


api.add_resource(ListObjectNamesResource, "/list-object-names")

if __name__ == "__main__":
    app.run(debug=True)
