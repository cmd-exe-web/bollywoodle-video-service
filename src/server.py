from flask import Flask
from flask_restful import Api

from flask_bcrypt import Bcrypt
from src.controllers.controller import (
    GenerateClipResource,
    SignupResource,
    LoginResource,
)
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

api = Api(app)
bcrypt = Bcrypt(app)
db = MongoEngine(app)
jwt = JWTManager(app)


api.add_resource(GenerateClipResource, "/generate-clip")
api.add_resource(SignupResource, "/auth/signup")
api.add_resource(LoginResource, "/auth/login")


if __name__ == "__main__":
    app.run(debug=True)
