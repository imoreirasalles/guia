from rest_framework import viewsets


from collection.models import Collection
from collection.api import serializers


class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects.filter(published=True)
    serializer_class = serializers.CollectionSerializer
