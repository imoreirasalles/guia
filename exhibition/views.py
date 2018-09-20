from datetime import date

from django.views.generic import ListView, DetailView

from home.mixins import OrderByMixin, SearchMixin
from location.models import Location
from .models import Exhibition


class ExhibitionListView(SearchMixin, OrderByMixin, ListView):
    queryset = Exhibition.objects.all()
    paginate_by = 20
    filters = (
        ('date_start', 'date_start__gte', date),
        ('date_end', 'date_end__lte', date),
        ('location', 'location__pk', int),
    )

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)

        location_ids = self.queryset.distinct('location').values_list('location__pk', flat=True)
        output['locations'] = [(location.pk, str(location)) for location in
                               Location.objects.filter(pk__in=location_ids)]
        return output


class ExhibitionDetail(DetailView):
    """Process each exhibition in details"""
    model = Exhibition

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
