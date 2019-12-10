import random
import json

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.utils.translation import ugettext_lazy as _

from .models import Collection


class CollectionList(ListView):
    model = Collection
    template_name = "collection/collection_list.html"
    context_object_name = "collections"

    def get_queryset(self):
        """Return the last five published questions."""
        return Collection.objects.order_by('updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        names = ("Coleção Gilberto Ferrez", "Arquivo Pixinguinha", "Biblioteca Clarice Lispector",
                 "Arquivo Millôr Fernandes", "Coleção Eduardo Coutinho")

        items = []
        for i in range(5):
            items.append({
                "label": names[i-1],
                "size": random.randint(20, 80),
                "url": "https://example.com",
            })

        context["jsonsample"] = json.dumps(items)

        return context


class CollectionDetail(DetailView):
    model = Collection
    template_name = "collection/collection_detail.html"
    context_object_name = "collection"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
