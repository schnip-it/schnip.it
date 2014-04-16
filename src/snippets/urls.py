from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views
from . import api_views

urlpatterns = patterns(
    '',
    url(r"^board/$", views.BoardList.as_view(), name="board_list"),
    url(r"^board/mine/$", views.BoardList.as_view(), name="board_list_mine",
        kwargs={"mine" : True}),
    url(r"^board/public/$", views.BoardList.as_view(), name="board_list_public",
        kwargs={"public" : True}),
    url(r"^board/new/$", login_required(views.BoardCreate.as_view()), name="board_create"),
    url(r"^board/(?P<pk>\d+)/$", views.BoardDetail.as_view(), name="board_detail"),
    url(r"^snippet/$", views.SnippetList.as_view(), name="snippet_list"),
    url(r"^snippet/new/$", login_required(views.SnippetCreate.as_view()), name="snippet_create"),
    url(r"^snippet/(?P<pk>\d+)/$", views.SnippetDetail.as_view(), name="snippet_detail"),
    url(r"^snippet/(?P<pk>\d+)/rate/$", login_required(views.SnippetRate.as_view()),
        name="snippet_rate"),

    url("^api/$", api_views.api_root),
    url(r"^api/snippet/$", api_views.SnippetList.as_view(), name="api-snippet_list"),
    url(r"^api/snippet/(?P<pk>\d+)/$", api_views.SnippetDetail.as_view(), name="api-snippet_detail"),
)
                       
