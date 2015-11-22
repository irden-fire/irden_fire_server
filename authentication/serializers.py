from django.contrib.auth.models import User
from rest_framework import serializers
from authentication.models import UserData

class UserSerializer(serializers.ModelSerializer):
    #userdata = serializers.StringRelatedField(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'userdata')

class UserDataSerializer(serializers.ModelSerializer):
    #userdata = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserData
        fields = ('full_name', 'phone_number', 'email', 'reg_date')
