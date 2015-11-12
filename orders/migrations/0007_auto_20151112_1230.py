# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20151112_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='desired_time',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
