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
