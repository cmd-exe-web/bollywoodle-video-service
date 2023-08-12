from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from src.controllers.controller import (
    GenerateClipResource,
    SignupResource,
    LoginResource,
)
from src.config import MONGO_URI, DATABASE_NAME
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
app.config["MONGODB_SETTINGS"] = {
    "db": DATABASE_NAME,
    "host": MONGO_URI,
}
app.config.from_envvar("ENV_FILE_LOCATION")
db = MongoEngine(app)
jwt = JWTManager(app)


api.add_resource(GenerateClipResource, "/generate-clip")
api.add_resource(SignupResource, "/auth/signup")
api.add_resource(LoginResource, "/auth/login")


if __name__ == "__main__":
    app.run(debug=True)
