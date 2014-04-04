from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Snippet, Board
from .forms import BoardForm

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
        return super().get_context_data(*args, **kwargs)

class SnippetCreate(generic.edit.CreateView):
    model = Snippet
    fields = ["title", "description", "language", "tags", "board", "code"]
    
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
    form_class = BoardForm
        
class BoardDetail(generic.detail.SingleObjectMixin, generic.ListView):
    paginate_by = 60
    template_name = "snippets/board_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Board.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snippets"] = self.object_list
        return context

    def get_queryset(self):
        return self.object.snippets.all()

