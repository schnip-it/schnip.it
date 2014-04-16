from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Snippet, Board
from .forms import BoardForm, SnippetForm

from ratings.views import RateView

class SnippetList(generic.ListView):
    model = Snippet
    context_object_name = "snippets"
    paginate_by = 12

    def get_queryset(self):
        r = self.request.user.profile.get_visible_snippets()

        if "q" in self.request.GET:
            r = r.filter(description__icontains=self.request.GET["q"])

        return r.order_by("-creation_time")

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

class OwnedCreateView(generic.edit.CreateView):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        print ("Form invalid! " + repr(form.__dict__))
        return super().form_invalid(form)

class SnippetCreate(OwnedCreateView):
    model = Snippet
    form_class = SnippetForm

class SnippetDetail(generic.DetailView):
    model = Snippet

class BoardList(generic.ListView):
    model = Board
    context_object_name = "boards"
    paginate_by = 60

    def get_context_data(self, *args, **kwargs):
        r = super().get_context_data(*args, **kwargs)
        r["mine"] = self.kwargs.get("mine", False)
        r["public"] = self.kwargs.get("public", False)
        return r

    def get_queryset(self):
        r = self.request.user.profile.get_visible_boards()

        if self.kwargs.get("mine", False):
            r = r.filter(owner_id=self.request.user.pk)

        if self.kwargs.get("public", False):
            r = r.filter(read_public=True)

        if "q" in self.request.GET:
            r = r.filter(name__icontains=self.request.GET["q"])

        return r.order_by("name")

class BoardCreate(OwnedCreateView):
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

class SnippetRate(RateView):
    model = Snippet

    def get_next_url(self):
        return reverse("snippet_detail", kwargs={"pk" : self.kwargs["pk"]})
