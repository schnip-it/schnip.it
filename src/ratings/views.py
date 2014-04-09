from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from .models import Rating

class RateView(View):
    next_url = None
    model = None

    def get_next_url(self):
        return self.next_url

    def get_model(self):
        return self.model

    def get(self, request, pk):
        return HttpResponseRedirect(self.get_next_url())
        
    def post(self, request, pk):
        model = self.get_model()
        pk = int(pk)
        user = request.user
        ct = ContentType.objects.get_for_model(model)
        
        get_object_or_404(model, pk=pk)

        try:
            rating = Rating.objects.get(content_type=ct,
                                        object_id=pk,
                                        user=user)
        except Rating.DoesNotExist:
            rating = Rating(content_type=ct, object_id=pk, user=user)
        
        try:
            rating.score = float(request.POST.get("score"))
            rating.save()
        except ValueError: pass

        return HttpResponseRedirect(self.get_next_url())
        

# Create your views here.
