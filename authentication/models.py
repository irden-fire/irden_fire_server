from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100, blank=True, default='')
    phone_number = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
