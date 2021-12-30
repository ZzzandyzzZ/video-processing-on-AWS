from datetime import datetime

from mongoengine import Document
from mongoengine.fields import DateTimeField
from mongoengine.fields import DecimalField
from mongoengine.fields import DictField
from mongoengine.fields import ListField
from mongoengine.fields import StringField


class Video(Document):
    created = DateTimeField(default=datetime.utcnow)
    name = StringField(required=True)
    duration = DecimalField(required=True)      # Minutes
    tags = ListField(DictField(), default=list)
    url = StringField(required=True)
