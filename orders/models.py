from django.db import models
from prices.models import Price
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=100, blank=True, default='')
    contact_number = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    email_status = models.CharField(max_length=100, blank=True, default='')
    price = models.ForeignKey(Price, related_name="price", default=0)

    def save(self, *args, **kwargs):
        """
        Send e-mail to current user and then save order
        """
        plaintext = get_template('emails/confirmation.txt')
        htmly     = get_template('emails/confirmation.html')
        d = Context({ 'client_name': self.client_name,  'program_name': self.price.name, 'cost': self.price.cost})
        subject, from_email, to = 'Hello from Irden', 'irden@gmail.com', self.email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        self.email_status = 'email sended'
        super(Order, self).save(*args, **kwargs)
