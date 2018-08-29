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
        qr                       = Collection.objects.all()

        descriptionlevel_filter = self.request.GET.get('descriptionlevel')
        if descriptionlevel_filter :
            if int(descriptionlevel_filter) > 0:
                qr = qr.filter(description_level=int(descriptionlevel_filter))

        accesscondition_filter = self.request.GET.get('accesscondition')
        if accesscondition_filter :
            if int(accesscondition_filter) > 0:
                qr = qr.filter(access_condition=int(accesscondition_filter))

        genretag_filter = self.request.GET.get('genretag')
        if genretag_filter :
            if int(genretag_filter) > 0:
                qr = qr.filter(genre_tags=int(genretag_filter))

        managementunit_filter = self.request.GET.get('managementunit')
        if managementunit_filter :
            if int(managementunit_filter) > 0:
                qr = qr.filter(management_unit=int(managementunit_filter))

        context['list']          = qr.order_by(self.get_ordering())
        
        context['now']           = timezone.now()
        context['order']         = self.order

        context['descriptionlevel_list'] = DescriptionLevel.objects.filter().order_by()
        context['accesscondition_list']  = AccessCondition.objects.filter().order_by()
        context['genretag_list']         = GenreTag.objects.filter().order_by()
        context['managementunit_list']   = ManagementUnit.objects.filter().order_by()

        return context


class CollectionDetail(DetailView):
    model = Collection
    template_name = "collection_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
