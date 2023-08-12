from ..config import db


class Video(db.Document):
    name = db.StringField(required=True, unique=True)
    url = db.URLField(required=False)
    s3_object_key = db.StringField(required=True, unique=True)
