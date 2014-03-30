from django.shortcuts import render

from snippets.models import Snippet

def home(req):
    return render(req, "snippets/home.html", {})
    
def snippet_read(req, snippet_id):
    return render(req, "snippets/read.html",
                  { 'snippet' : get_object_or_404(Snippet, id=snippet_id) })

def tos(req):
    return render(req, "snippets/home.html", {})
