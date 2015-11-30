from rest_framework import serializers

from django.contrib.auth.models import User
from orders.models import Order
from orders.serializers import OrderSerializer
from authentication.models import UserData

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class UserSerializerCreate(serializers.ModelSerializer):
#    userdata = UserDataSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'password')

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
            user = User(username=user_info['username'])
            user.set_password(user_info['password'])
            user.save()
            """
            #Send email to current user
            """
            plaintext = get_template('emails/user_was_created.txt')
            htmly     = get_template('emails/user_was_created.html')
            d = Context({   'username': user_info['username'],
                            'password': user_info['password'],
                            'fullname': validated_data['client_name']})
            subject, from_email, to = 'User successfully created', 'irdenfire@gmail.com', validated_data['email']
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            user_data = UserData.objects.create(user = user, **validated_data)            
        else:
            user_data = UserData.objects.create(**validated_data)

        Order.objects.create(user_data = user_data, **order_info[0])
        return user_data

    def update(self, instance, validated_data):
        order_info = validated_data.pop('orders')
        instance.client_name = validated_data.get('client_name', instance.email)
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        Order.objects.create(user_data = instance, **order_info[0])
        return instance
