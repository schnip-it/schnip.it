from django.shortcuts import render

def home(req):
    return render(req, "snippets/home.html", {})
