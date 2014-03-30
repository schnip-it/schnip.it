from django import forms
from account.forms import SettingsForm

class ProfileSettingsForm(SettingsForm):
    bio = forms.CharField(widget=forms.Textarea)
