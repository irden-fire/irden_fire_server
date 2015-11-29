from django.db import models
from prices.models import Price
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

from authentication.models import UserData

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100, blank=True, default='')
    contact_number = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    email_status = models.CharField(max_length=100, blank=True, default='')
    price = models.ForeignKey(Price, related_name="price", default=0)
    desired_date = models.DateTimeField(default=datetime.now, blank=True)
    user_data = models.ForeignKey(UserData, blank=True, null=True, related_name='orders')
