from django.views.generic import ListView
from .models import Exhibition


class ExhibitionListView(ListView):
    queryset = Exhibition.objects.all()
    paginate_by = 2