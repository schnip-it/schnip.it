from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name="profile")
    bio = models.TextField(blank=True)

    def __str__(self):
        return "<UserProfile for {}>".format(self.user)

def create_user_profile(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user = instance)

models.signals.post_save.connect(create_user_profile, sender=User)
