from django.db.models import Model, PositiveIntegerField, FloatField, ForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generics import GenericKey
from django.contrib.auth.models import User

class Rating(Model):
    content_type = ForeignKey(ContentType)
    object_id = PositiveIntegerField()
    object = GenericKey()
    user = ForeignKey(User)
    score = FloatField()

    def __str__(self):
        return "{} = {} ({})".format(object, score, user)
