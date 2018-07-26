# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Project guia imports
from .models import *



class CollectionList(ListView):
    model = Collection
    paginate_by = 10
    context_object_name = "collection_list"
    template_name = "collection_list.html"

    def get_ordering(self):
        self.order = self.request.GET.get('order', 'asc')
        selected_ordering = self.request.GET.get('order_by', 'title')
        if self.order == "desc":
            selected_ordering = "-" + selected_ordering
        return selected_ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['current_order'] = self.get_ordering()
        context['order'] = self.order
        return context


class CollectionDetail(DetailView):
    model = Collection
    template_name = "collection_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
