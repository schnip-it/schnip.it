from django.shortcuts import render
from django.views import generic
from . import forms

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

class Contact(generic.FormView):
    template_name = "shnipit/contact_form.html"
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send_email()
        return render(self.request,
                      "shnipit/contact_success.html",
                      form.cleaned_data)

