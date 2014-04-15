from django import forms
from account.forms import SettingsForm

class ProfileSettingsForm(SettingsForm):
    bio = forms.CharField(widget=forms.Textarea)
    avatar = forms.ImageField()
    sub1 = forms.CharField()
    sub2 = forms.CharField()
