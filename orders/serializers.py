from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'created', 'price', 'desired_date', 'user_data')
