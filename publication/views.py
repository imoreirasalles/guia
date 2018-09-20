from datetime import date

from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from home.mixins import OrderByMixin, SearchMixin
from .models import *


class PublicationListView(SearchMixin, OrderByMixin, ListView):
    queryset = Publication.objects.all()
    paginate_by = 20
    filters = (
        ('date_released', 'date_released', date),
        ('title', 'title__icontains', str),
        ('type', 'type__pk', int),
    )

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)
        output['types'] = PublicationType.objects.values_list('pk', 'title')
        return output


class CollectionDetail(DetailView):
    """Process each collection in details"""
    model = Publication
    template_name = "publication_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
