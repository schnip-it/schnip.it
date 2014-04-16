from .models import Snippet, Board
from .serializers import SnippetSerializer
import rest_framework as rest
from rest_framework import generics, decorators
from django.core.urlresolvers import reverse

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

@decorators.api_view(["GET"])
def api_root(request, format=None):
    return rest.response.Response({
        "snippet" : reverse("api-snippet_list")
    })
