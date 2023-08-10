from flask_restful import Resource
from src.services.s3_service import S3Service


class ListObjectNamesResource(Resource):
    def get(self):
        try:
            s3_service = S3Service()
            object_names = s3_service.retrieve_object_names()
            return {"object_names": object_names}, 200
        except Exception as e:
            return {"error": str(e)}, 500
