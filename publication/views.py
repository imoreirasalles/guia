# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Project guia imports
from .models import *


class PublicationList(ListView):
    """CBV to list and process filter into all Publications"""
    model = Publication
    paginate_by = 10
    context_object_name = "publication_list"
    template_name = "publication_list.html"

    def get_ordering(self):
        self.order = self.request.GET.get('order', 'asc')
        selected_ordering = self.request.GET.get('order_by', 'title')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_queryset(self):
        queryset = Publication.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CollectionDetail(DetailView):
    """Process each collection in details"""
    model = Publication
    template_name = "publication_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
