from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    #user = models.OneToOneField(User, primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100, blank=True, default='')
    contact_number = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.reg_date.strftime("%Y-%m-%d %H:%M:%S") + " " + self.email
