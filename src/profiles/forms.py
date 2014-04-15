from django import forms
from account.forms import SettingsForm

class ProfileSettingsForm(SettingsForm):
    bio = forms.CharField(widget=forms.Textarea, blank=True)
    avatar = forms.ImageField(blank=True)
    sub1 = forms.CharField(blank=True)
    sub2 = forms.CharField(blank=True)
