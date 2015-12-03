from rest_framework import serializers
from prices.models import Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Price
        fields = ('id', 'created', 'name', 'cost', 'duration', 'how_many_participants', 'description', 'description_l18n')
