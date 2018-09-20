from django.views.generic import ListView, DetailView
from .models import Exhibition
from location.models import Location
from datetime import datetime
from home.mixins import OrderByMixin


class ExhibitionListView(OrderByMixin, ListView):
    queryset = Exhibition.objects.all()
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)

        location_ids = self.queryset.distinct('location').values_list('location__pk', flat=True)
        output['locations'] = [(location.pk, str(location)) for location in
                               Location.objects.filter(pk__in=location_ids)]
        return output

    def get_queryset(self):
        queryset = super().get_queryset()

        date_start = self.request.GET.get('date_start')
        date_end = self.request.GET.get('date_end')
        location = self.request.GET.get('location')

        if date_start:
            try:
                date = datetime.strptime(date_start, "%d/%m/%Y")
                queryset = queryset.filter(date_start__gte=date)
            except ValueError:
                pass

        if date_end:
            try:
                date = datetime.strptime(date_end, "%d/%m/%Y")
                queryset = queryset.filter(date_end__lte=date)
            except ValueError:
                pass

        if location:
            queryset = queryset.filter(location__pk=location)

        return queryset


class ExhibitionDetail(DetailView):
    """Process each exhibition in details"""
    model = Exhibition

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
