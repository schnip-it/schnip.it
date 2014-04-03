from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Snippet, Board

class SnippetList(generic.ListView):
    model = Snippet
    context_object_name = "snippets"
    paginate_by = 12

    def get_queryset(self):
        r = Snippet.objects
        
        if "q" in self.request.GET:
            r = r.filter(description__icontains=self.request.GET["q"])
            
        return r.order_by("-creation_time")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        print (context)

        return context

class SnippetCreate(generic.edit.CreateView):
    model = Snippet

class SnippetDetail(generic.DetailView):
    model = Snippet

class BoardList(generic.ListView):
    model = Board
    context_object_name = "boards"
    paginate_by = 12

    def get_queryset(self):
        r = Board.objects
        
        if "q" in self.request.GET:
            r = r.filter(name__icontains=self.request.GET["q"])
            
        return r.order_by("name")
    
class BoardCreate(generic.edit.CreateView):
    model = Board

class BoardDetail(generic.DetailView):
    model = Board
    paginate_by = 60

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object.snippets.all(), self.paginate_by)
        
        try:
            page = paginator.page(self.request.GET.get("page"))
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        context["snippets"] = page
        return context
        
