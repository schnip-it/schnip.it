from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["name", "read_public", "read_users",
                  "write_public", "write_users"]
        widgets = {
            "read_users" : forms.CheckboxSelectMultiple(),
            "write_users" : forms.CheckboxSelectMultiple(),
        }
