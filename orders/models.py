from django.db import models
from prices.models import Price
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100, blank=True, default='')
    contact_number = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    email_status = models.CharField(max_length=100, blank=True, default='')
    price = models.ForeignKey(Price, related_name="price", default=0)
    desired_date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        """
        Send e-mail to current user
        """
        plaintext = get_template('emails/confirmation.txt')
        htmly     = get_template('emails/confirmation.html')
        d = Context({   'client_name': self.client_name,
                        'program_name': self.price.name,
                        'cost': self.price.cost})
        subject, from_email, to = 'Your order was processed', 'irdenfire@gmail.com', self.email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        """
        Send e-mail to admins
        """
        plaintext = get_template('emails/to_admins.txt')
        htmly     = get_template('emails/to_admins.html')
        d = Context({   'client_name': self.client_name,
                        'program_name': self.price.name,
                        'cost': self.price.cost,
                        'phone_number': self.contact_number,
                        'program_id': self.price.pk,
                        'desired_date': self.desired_date
                        })
        subject, from_email, to = 'Attention, new order was placed', 'irdenfire@gmail.com', ['forrana@gmail.com', 'forrana@yandex.ru']
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        """
        Set status to 'sended' and save record
        """
        self.email_status = 'Sended'
        super(Order, self).save(*args, **kwargs)
