from django.conf import settings
from django.forms import widgets
from rest_framework import serializers
from .models import Snippet

    # creation_time = models.DateField(auto_now_add=True)
    # title = models.CharField(max_length=255)
    # description = models.TextField()
    # owner = models.ForeignKey(User, related_name="snippets")
    # board = models.ForeignKey(Board, related_name="snippets")
    # language = models.CharField(max_length=255, choices=SNIPPET_LANGUAGES)
    # code = models.TextField()
    # tags = TaggableManager()
    # ratings = GenericRelation(Rating)
    
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "description", "owner", "board", "language", "code"]
