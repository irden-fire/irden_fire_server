from rest_framework import serializers

from django.contrib.auth.models import User
from orders.models import Order
from orders.serializers import OrderSerializer
from authentication.models import UserData

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class UserSerializerCreate(serializers.ModelSerializer):
#    userdata = UserDataSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password')

#    def create(self, validated_data):
#        user = User.objects.create_user(**validated_data)
#        return user
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDataSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    user = UserSerializer(required=False)

    class Meta:
        model = UserData
        fields = ('pk', 'client_name', 'contact_number', 'email', 'user', 'orders')

    def create(self, validated_data):
        order_info = validated_data.pop('orders')

        if 'user' in validated_data:
            user_info = validated_data.pop('user')
            #user = User.objects.create(**user_info)
            user = User(username=user_info['username'])
            user.set_password(user_info['password'])
            user.save()
            user_data = UserData.objects.create(user = user, **validated_data)
        else:
            user_data = UserData.objects.create(**validated_data)

        Order.objects.create(user_data = user_data, **order_info[0])
        return user_data
