from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="boards")
    read_public = models.BooleanField()
    write_public = models.BooleanField()
    read_users = models.ManyToManyField(User, related_name="readable", blank=True)
    write_users = models.ManyToManyField(User, related_name="writeable", blank=True)

    def __str__(self): return self.name

class Snippet(models.Model):
    creation_time = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    board = models.ForeignKey(Board)
    code = models.TextField()
    tags = TaggableManager()

    def __str__(self): return self.title
