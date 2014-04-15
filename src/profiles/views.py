from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from account.views import SettingsView
from .forms import ProfileSettingsForm


class ProfileSettingsView(SettingsView):
    form_class = ProfileSettingsForm
    
    def update_account(self, form):
        super(ProfileSettingsView, self).update_account(form)

        print (dir(form))
        
        profile = self.request.user.profile
        profile.bio = form.cleaned_data["bio"]
        profile.avatar = form.cleaned_data["avatar"]
        profile.save()

    def get_initial(self):
        initial = super(ProfileSettingsView, self).get_initial()
        initial["bio"] = self.request.user.profile.bio
        initial["avatar"] = self.request.user.profile.avatar
        return initial

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class ProfileDetailView(DetailView):
    model = User
    context_object_name = "profile_user"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if "pk" not in kwargs:
            self.kwargs["pk"] = request.user.pk
            kwargs["pk"] = request.user.pk

        return super().get(request, *args, **kwargs)
