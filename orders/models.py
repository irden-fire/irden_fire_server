from django.db import models
from prices.models import Price
from django.core.mail import send_mail
from django.core.mail import EmailMessage

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100, blank=True, default='')
    contact_number = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    email_status = models.CharField(max_length=100, blank=True, default='')
    price = models.ForeignKey(Price, related_name="price", default=0)

    def save(self, *args, **kwargs):
        """
        Send e-mail to current user
        """
        email = EmailMessage('Irden', 'Irden', to=['forrana@gmail.com'])
        email.send()
        self.email_status = 'email sended'
        super(Order, self).save(*args, **kwargs)
