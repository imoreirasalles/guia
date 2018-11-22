from datetime import date

from guia.views import BaseDraftDetailView, BaseDraftListView
from home.mixins import OrderByMixin, SearchMixin

from .models import Person


class PersonListView(SearchMixin, OrderByMixin, BaseDraftListView):
    model = Person
    paginate_by = 20
    filters = (
        ('date_start', 'date_start__gte', date),
        ('date_end', 'date_end__lte', date),
        ('title', 'title__icontains', str),
        ('gender', 'gender', str),
        ('is_staff', 'is_staff', bool),
        ('is_partner', 'is_partner', bool),
        ('is_feature', 'is_feature', bool),
    )

    def get_context_data(self, *args, **kwargs):
        output = super().get_context_data(*args, **kwargs)
        output['genders'] = Person.objects.published().distinct('gender').values_list('gender', flat=True)
        return output


class PersonDetailView(BaseDraftDetailView):
    model = Person
