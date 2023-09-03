from flask_restful import Resource, reqparse
from src.services.video_clip_service import VideoClipService
from src.models.user import User
import datetime
from flask_jwt_extended import create_access_token
import uuid
from src.constants import NUM_FRAMES_TO_COLLECT, SAVE_VIDEO_PATH
from src.services.s3_service import S3Service
from src.models.video import Video

user_parser = reqparse.RequestParser()
user_parser.add_argument(
    "username", type=str, required=True, help="Username is required"
)
user_parser.add_argument(
    "password", type=str, required=True, help="Password is required"
)

video_parser = reqparse.RequestParser()
video_parser.add_argument(
    "video_url", type=str, required=True, help="Video URL is required"
)
video_parser.add_argument(
    "video_name", type=str, required=True, help="Video name is required"
)


class GenerateClipResource(Resource):
    def post(self):
        args = video_parser.parse_args()
        video_url = args["video_url"]
        video_name = args["video_name"]
        try:
            uuid1 = uuid.uuid4()
            save_path = SAVE_VIDEO_PATH.format(uuid1)
            VideoClipService().create_and_save_clip(
                video_url, save_path, NUM_FRAMES_TO_COLLECT, str(uuid1)
            )
            S3Service().upload_object(save_path)
            Video(name=video_name, url=video_url, s3_object_key=str(uuid1)).save()

            return {"success": True}, 200
        except Exception as e:
            return {"error": str(e)}, 500


class SignupResource(Resource):
    def post(self):
        try:
            args = user_parser.parse_args()
            print(args)
            user = User(**args)
            user.hash_password()
            user.save()
            id = user.id
            return {"id": str(id)}, 201
        except Exception as e:
            return {"error": str(e)}, 500


class LoginResource(Resource):
    def post(self):
        args = user_parser.parse_args()
        print(args)
        user = User.objects.get(username=args.get("username"))
        authorized = user.check_password(args.get("password"))
        if not authorized:
            return {"error": "Username or password invalid"}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {"token": access_token}, 200
