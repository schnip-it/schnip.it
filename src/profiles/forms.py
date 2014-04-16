from django import forms
from account.forms import SettingsForm

class ProfileSettingsForm(SettingsForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    avatar = forms.ImageField(required=False)
    sub1 = forms.CharField(required=False)
    sub2 = forms.CharField(required=False)
