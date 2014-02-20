from django.contrib import admin
from snippets.models import *

for cls in (Board, Snippet):
    admin.site.register(cls)
