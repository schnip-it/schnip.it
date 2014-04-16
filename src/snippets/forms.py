from django import forms
from .models import Board, Snippet

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["name", "owner", "read_public", "read_users",
                  "write_public", "write_users"]
        exclude = ["owner"]
        widgets = {
            "read_users" : forms.CheckboxSelectMultiple(),
            "write_users" : forms.CheckboxSelectMultiple(),
        }

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ["title", "description", "language", "tags", "board", "code", "owner"]
        exclude = ["owner"]
