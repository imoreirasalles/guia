from rest_framework import viewsets


from vocabulary.models import Term
from vocabulary.api import serializers


class TermViewset(viewsets.ModelViewSet):
    queryset = Term.objects.filter(published=True)
    serializer_class = serializers.TermSerializer
