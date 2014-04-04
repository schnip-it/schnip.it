from django.conf.urls import patterns, include, url

from profiles.views import ProfileSettingsView
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^$", views.home, name="home"),
    url(r"^tos/$", views.tos, name="tos"),
    url(r"^help/$", views.help, name="help"),
    url(r"^about/$", views.about, name="about"),
    url(r"^privacy/$", views.privacy, name="privacy"),
    url(r"^contact/$", views.Contact.as_view(), name="contact"),
    url(r"^", include("snippets.urls")),
)
