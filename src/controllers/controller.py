from flask import request
from flask_restful import Resource
from src.services.s3_service import S3Service
from src.services.video_clip_service import VideoClipService


class ListObjectNamesResource(Resource):
    def get(self):
        try:
            s3_service = S3Service()
            object_names = s3_service.retrieve_object_names()
            return {"object_names": object_names}, 200
        except Exception as e:
            return {"error": str(e)}, 500


class VideoClipResource(Resource):
    def get(self):
        try:
            video_url = request.headers.get("Video-Url")

            if video_url is None:
                return {"error": "Video-Url header not found in the request."}, 400

            save_video_path = "./video5.mp4"
            num_frames_to_collect = 50
            clip_service = VideoClipService()
            print("Download the video clip")  # Remove in prod
            clip_service.create_and_save_clip(
                video_url, save_video_path, num_frames_to_collect
            )

            return {"success": True}, 200
        except Exception as e:
            return {"error": str(e)}, 500
