from django.contrib import admin
from snippets.models import *

for cls in (Tag, Board, Snippet):
    admin.site.register(cls)
