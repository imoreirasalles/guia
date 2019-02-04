from datetime import date

from django.db.models import Q

from guia.views import BaseDraftListView, BaseDraftDetailView
from home.mixins import OrderByMixin, SearchMixin
from location.models import Location

from .models import Exhibition


class ExhibitionListView(SearchMixin, OrderByMixin, BaseDraftListView):
    model = Exhibition
    paginate_by = 20

    filters = (
        ('date_start', 'date_start__gte', date),
        ('date_end', 'date_end__lte', date),
        ('location', 'locations', int),
    )

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'date_start')
        # validate ordering here
        return ordering

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title', None)

        if title:
            return queryset.filter(Q(Q(title__icontains=title) | Q(abstract__icontains=title)))

        return queryset
        # .objects.order_by('-date_start')

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)
        queryset = self.get_queryset()
        location_ids = queryset.distinct('locations').values_list('locations__pk', flat=True)
        output['locations'] = [(location.pk, str(location)) for location in
                               Location.objects.filter(pk__in=location_ids)]
        return output


class ExhibitionDetailView(BaseDraftDetailView):
    """Process each exhibition in details"""
    model = Exhibition
