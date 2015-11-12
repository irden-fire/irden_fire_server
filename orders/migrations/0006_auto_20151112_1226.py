# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_email_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='desired_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='desired_time',
            field=models.CharField(default=b'', max_length=6, blank=True),
        ),
    ]
