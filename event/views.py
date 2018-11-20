from datetime import date

from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from guia.views import BaseDraftDetailView, BaseDraftListView
from home.mixins import OrderByMixin, SearchMixin
from .models import Event, EventType
from location.models import Location


class EventListView(SearchMixin, OrderByMixin, BaseDraftListView):
    model = Event
    paginate_by = 20
    filters = (
        ('title', 'title__icontains', str),
        ('type', 'type__pk', int),
        ('date_start', 'date_start__gte', date),
        ('date_end', 'date_end__lte', date),
        ('location', 'location__pk', int),
    )

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)
        output['types'] = EventType.objects.values_list('pk', 'title')
        output['locations'] = Location.objects.values_list('pk', 'title')
        return output


class EventDetailView(BaseDraftDetailView):
    model = Event
