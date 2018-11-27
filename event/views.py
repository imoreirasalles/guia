from datetime import date

from django.db.models import Q

from location.models import Location

from guia.views import BaseDraftDetailView, BaseDraftListView
from home.mixins import OrderByMixin, SearchMixin
from .models import Event, EventType


class EventListView(SearchMixin, OrderByMixin, BaseDraftListView):
    model = Event
    paginate_by = 20
    filters = (
        ('type', 'type__pk', int),
        ('date_start', 'date_start__gte', date),
        ('date_end', 'date_end__lte', date),
        ('location', 'location__pk', int),
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title', None)

        if title:
            return queryset.filter(Q(Q(title__icontains=title) | Q(abstract__icontains=title)))

        return queryset

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)
        output['types'] = EventType.objects.values_list('pk', 'title')
        output['locations'] = Location.objects.values_list('pk', 'title')
        return output


class EventDetailView(BaseDraftDetailView):
    model = Event
