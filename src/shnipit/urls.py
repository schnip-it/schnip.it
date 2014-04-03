from django.conf.urls import patterns, include, url

from profiles.views import ProfileSettingsView
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^$", views.home),
    url(r"^tos/$", views.tos),
    url(r"^help/$", views.help),
    url(r"^about/$", views.about),
    url(r"^privacy/$", views.privacy),
    url(r"^contact/$", views.contact),
    url(r"^", include("snippets.urls")),
)
