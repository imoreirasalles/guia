from rest_framework import serializers


from vocabulary.models import Term


class TermSerializer(serializers.ModelSerializer):
    id = serializers.URLField(source='semantic_url')
    data = serializers.JSONField(source='extra')

    class Meta:
        model = Term
        fields = ('id', 'label', 'summary', 'data')
