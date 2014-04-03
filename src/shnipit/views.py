from django.shortcuts import render

def home(req):
    return render(req, "shnipit/home.html", {})
    
def tos(req):
    return render(req, "shnipit/tos.html", {})

def about(req):
    return render(req, "shnipit/about.html", {})

def help(req):
    return render(req, "shnipit/help.html", {})

def privacy(req):
    return render(req, "shnipit/privacy.html", {})

def contact(req):
    return render(req, "shnipit/contact.html", {})
