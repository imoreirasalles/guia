from rest_framework import serializers


from collection.models import Collection
from vocabulary.api.serializers import TermSerializer


class CollectionSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(source='id_human')
    startDate = serializers.DateField(source='start_date')
    endDate = serializers.DateField(source='end_date')
    availableByRequest = serializers.IntegerField(source='progress_technical')
    availableOnline = serializers.IntegerField(source='progress_online')
    numberOfItems = serializers.IntegerField(source='items_total')
    aggregation_type = TermSerializer(read_only=True, many=True)
    people = TermSerializer(read_only=True, many=True, source='featured_people')

    class Meta:
        model = Collection
        fields = ('uuid', 'identifier', 'label', 'summary', 'startDate',
                  'endDate', 'numberOfItems', 'availableByRequest', 'availableOnline', 'aggregation_type', 'people')
