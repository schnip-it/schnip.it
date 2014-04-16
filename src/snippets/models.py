from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.generic import GenericRelation

from taggit.managers import TaggableManager
from ratings.models import Rating
from shnipit.settings import SNIPPET_LANGUAGES

class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="boards")
    read_public = models.BooleanField()
    write_public = models.BooleanField()
    read_users = models.ManyToManyField(User, related_name="readable_boards", blank=True)
    write_users = models.ManyToManyField(User, related_name="writeable_boards", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("board_detail", kwargs={"pk" : self.pk})

    @staticmethod
    def get_visible(user):
        return Board.objects.filter(Q(readable_users=self.user)
                                    | Q(owner=self.user))
        
class Snippet(models.Model):
    creation_time = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name="snippets")
    board = models.ForeignKey(Board, related_name="snippets")
    language = models.CharField(max_length=255, choices=SNIPPET_LANGUAGES)
    code = models.TextField()
    tags = TaggableManager()
    ratings = GenericRelation(Rating)

    def __str__(self):
        return self.title

    @staticmethod
    def get_visible(user):
        return Board.objects.filter(Q(board__readable_users=self.user)
                                    | Q(owner=self.user))
        
    def get_absolute_url(self):
        return reverse("snippet_detail", kwargs={"pk" : self.pk})

    def get_mean_rating(self):
        sum = 0.0
        count = 0

        for rating in self.ratings.all():
            sum += rating.score
            count += 1

        if count: return sum / count

        return 0

    def get_divisions(self, n = 5):
        return [x / (n - 1) for x in range(n)]
