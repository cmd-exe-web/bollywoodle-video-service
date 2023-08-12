import os
import boto3
from ..config import AWS_ACCESS_KEY, AWS_SECRET_KEY
from ..constants import BUCKET_NAME


class S3Service:
    def __init__(self):
        self.s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        self.bucket = self.s3_resource.Bucket(BUCKET_NAME)

    def retrieve_object_names(self):
        object_names = [obj.key for obj in self.bucket.objects.all()]
        return object_names

    def upload_object(self, file_name):
        # os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        # file_path = os.path.join(root_dir, file_name)
        absolute_path = os.path.abspath(file_name)
        object_name = os.path.basename(file_name)

        self.bucket.upload_file(absolute_path, object_name)
