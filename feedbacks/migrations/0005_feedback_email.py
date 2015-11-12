# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20151108_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
