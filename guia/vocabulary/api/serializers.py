from rest_framework import serializers


from vocabulary.models import Term


class TermSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='semantic_url')
    data = serializers.JSONField(source='extra')

    class Meta:
        model = Term
        fields = ('uuid', 'url', 'label', 'summary', 'data')
