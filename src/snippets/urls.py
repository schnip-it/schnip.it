from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r"^board/$", views.BoardList.as_view(), name="board_list"),
    url(r"^board/new$", views.BoardCreate.as_view(), name="board_create"),
    url(r"^board/(?P<pk>\d+)/$", views.BoardDetail.as_view(), name="board_detail"),
    url(r"^snippet/$", views.SnippetList.as_view(), name="snippet_list"),
    url(r"^snippet/new/$", views.SnippetCreate.as_view(), name="snippet_create"),
    url(r"^snippet/(?P<pk>\d+)/$", views.SnippetDetail.as_view(), name="snippet_detail"),
)
                       
