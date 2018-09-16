# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Project guia imports
from .models import *
from glossary.models import DescriptionLevel
from glossary.models import AccessCondition
from glossary.models import GenreTag
from management.models import ManagementUnit



class CollectionList(ListView):
    """CBV to list and process filter into all Collections"""
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

    def get_queryset(self):
        queryset = Collection.objects.all()
        management_unit_list = self.request.GET.getlist('management_unit')
        description_level_list = self.request.GET.getlist('description_level')
        access_condition_list = self.request.GET.getlist('access_condition')
        genre_tag_list = self.request.GET.getlist('genre_tag')

        if (management_unit_list and int(management_unit_list[0]) > 0):
            queryset = queryset.filter(management_unit__in=management_unit_list)

        if (description_level_list and int(description_level_list[0]) > 0):
            queryset = queryset.filter(description_level__in=description_level_list)

        if (access_condition_list and int(access_condition_list[0]) > 0):
            queryset = queryset.filter(access_condition__in=access_condition_list)

        if (genre_tag_list and int(genre_tag_list[0]) > 0):
            queryset = queryset.filter(description_level__in=genre_tag_list)

        queryset = queryset.order_by(self.get_ordering())
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.order
        context['management_unit_list']   = ManagementUnit.objects.filter().order_by()
        context['description_level_list'] = DescriptionLevel.objects.filter().order_by()
        context['access_condition_list']  = AccessCondition.objects.filter().order_by()
        context['genre_tag_list'] = GenreTag.objects.filter().order_by()

        context['management_unit_selected'] = list(map(int, self.request.GET.getlist('management_unit')))

        context['description_level_selected'] = list(map(int, self.request.GET.getlist('description_level')))

        context['access_condition_selected'] = list(map(int, self.request.GET.getlist('access_condition')))

        context['genre_tag_selected'] = list(map(int, self.request.GET.getlist('genre_tag')))

        return context


class CollectionDetail(DetailView):
    """Process each collection in details"""
    model = Collection
    template_name = "collection_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CollectionSearchList(CollectionList):
    """docstring for [object Object]."""
    model = Collection
    template_name = "collection_detail.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
