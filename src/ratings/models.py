from django.db.models import Model, PositiveIntegerField, FloatField, ForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.auth.models import User

class Rating(Model):
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()
    user = ForeignKey(User)
    score = FloatField()

    def __str__(self):
        return "{} = {} ({})".format(content_object, score, user)
