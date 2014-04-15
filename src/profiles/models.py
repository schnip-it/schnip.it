from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from snippets.models import Board

class UserProfile(models.Model):
    user   = models.OneToOneField(User, unique=True, related_name="profile")
    avatar = models.ImageField(upload_to="profiles/avatars", null=True, blank=True)
    bio    = models.TextField(blank=True)
    sub1   = models.TextField(blank=True)
    sub2   = models.TextField(blank=True)

    def __str__(self):
        return "<UserProfile for {}>".format(self.user)

    def own_boards(self):
        return Board.objects.filter(owner=self.user)

    def own_public_boards(self):
        return Board.objects.filter(owner=self.user, read_public=True)

    def get_absolute_url(self):
        return reverse("account_profile", pk=self.pk)
        
def create_user_profile(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=User)
