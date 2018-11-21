from datetime import date

from django.utils import timezone

from guia.views import BaseDraftDetailView, BaseDraftListView

from home.mixins import OrderByMixin, SearchMixin
from .models import Publication, PublicationType


class PublicationListView(SearchMixin, OrderByMixin, BaseDraftListView):
    model = Publication
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


class PublicationDetailView(BaseDraftDetailView):
    """Process each collection in details"""
    model = Publication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
