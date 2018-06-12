from django.conf import settings
from django.conf.urls.static import static
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from core.models import *
from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


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


def exhibition(request):
    return render(request, 'exhibition.html')


def publication(request):
    return render(request, 'publication.html')


def person(request):
    return render(request, 'person.html')
