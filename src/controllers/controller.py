from flask import request
from flask_restful import Resource, reqparse
from src.services.s3_service import S3Service
from src.services.video_clip_service import VideoClipService
from src.services.mongodb_service import DocumentService
from src.models.user import User


class ListObjectNamesResource(Resource):
    def get(self):
        try:
            s3_service = S3Service()
            object_names = s3_service.retrieve_object_names()
            return {"object_names": object_names}, 200
        except Exception as e:
            return {"error": str(e)}, 500


class GenerateClip(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "video_urlfex", type=str, required=True, help="Video URL is required"
        )
        args = parser.parse_args()

        video_url = args["video_url"]
        print(video_url)
        try:
            save_video_path = "./video7.mp4"
            num_frames_to_collect = 50
            clip_service = VideoClipService()
            clip_service.create_and_save_clip(
                video_url, save_video_path, num_frames_to_collect
            )

            return {"success": True}, 200
        except Exception as e:
            return {"error": str(e)}, 500


class S3Resource(Resource):
    def post(self, file_name):
        try:
            s3_service = S3Service()
            s3_service.upload_object(file_name)
            return {"message": "File uploaded successfully"}, 201
        except Exception as e:
            return {"message": str(e)}, 500


class MongoDbResource(Resource):
    def post(self, document_name):
        DocumentService.add_document(document_name)
        return {"message": f'Document "{document_name}" added to collection'}, 201


class SignupApi(Resource):
    def post(self):
        try:
            # import ipdb
            # ipdb.set_trace()
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {"id": str(id)}, 201
        except Exception as e:
            return {"error": str(e)}, 500
