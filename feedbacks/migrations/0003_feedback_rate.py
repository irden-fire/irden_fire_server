# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_auto_20151105_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(default=10),
        ),
    ]
