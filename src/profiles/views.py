from django.shortcuts import render
from account.views import SettingsView
from .forms import ProfileSettingsForm

class ProfileSettingsView(SettingsView):
    form_class = ProfileSettingsForm

    def update_account(self, form):
        super(ProfileSettingsView, self).update_account(form)
        
        if "bio" in form.cleaned_data:
            profile = self.request.user.profile
            profile.bio = form.cleaned_data["bio"]
            profile.save()

    def get_initial(self):
        initial = super(ProfileSettingsView, self).get_initial()
        initial["bio"] = self.request.user.profile.bio
        return initial
