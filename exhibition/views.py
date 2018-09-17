from django.views.generic import ListView
from .models import Exhibition
from location.models import Location
from datetime import datetime


class ExhibitionListView(ListView):
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

        date = self.request.GET.get('date')
        location = self.request.GET.get('location')

        if date:
            date = datetime.strptime(date, "%d/%m/%Y")
            queryset = queryset.filter(date_start__gte=date, date_end__lte=date)

        if location:
            queryset = queryset.filter(location__pk=location)

        return queryset
