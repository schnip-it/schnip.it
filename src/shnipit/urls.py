from django.conf.urls import patterns, include, url

from profiles.views import ProfileSettingsView, ProfileDetailView
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/settings/$", ProfileSettingsView.as_view(), name="account_settings"),
    url(r"^account/profile/$", ProfileDetailView.as_view(), name="account_my_profile"),
    url(r"^account/profile/(?P<pk>\d+)/$", ProfileDetailView.as_view(),
        name="account_profile"),
    url(r"^account/", include("account.urls")),
    url(r"^$", views.home, name="home"),
    url(r"^tos/$", views.tos, name="tos"),
    url(r"^help/$", views.help, name="help"),
    url(r"^about/$", views.about, name="about"),
    url(r"^team/$", views.team, name="team"),
    url(r"^privacy/$", views.privacy, name="privacy"),
    url(r"^contact/$", views.Contact.as_view(), name="contact"),
    url(r"^", include("snippets.urls")),
)
