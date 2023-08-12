import mongoengine as me


class Video(me.Document):
    name = me.StringField(required=True, unique=True)
    url = me.URLField(required=False)
    s3_object_key = me.StringField(required=True, unique=True)
