from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name="index"),
    url(r'^/tos/$', views.tos, name="terms_of_service"))
                       
