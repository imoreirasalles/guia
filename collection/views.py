# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Project guia imports
from .models import *

def collection(request):
    return render(request, 'collection.html')


class CollectionList(ListView):
    model = Collection
    paginate_by = 30
    template_name = "collection.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CollectionDetail(DetailView):
    model = Collection
    template_name = "collection_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
