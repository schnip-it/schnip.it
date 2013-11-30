from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self): return self.name

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
    tags = models.ManyToManyField(Tag)
    score = models.FloatField(default=0)
    score0 = models.PositiveIntegerField(default=0)
    score1 = models.PositiveIntegerField(default=0)
    score2 = models.PositiveIntegerField(default=0)
    score3 = models.PositiveIntegerField(default=0)
    score4 = models.PositiveIntegerField(default=0)

    def __str__(self): return self.title
