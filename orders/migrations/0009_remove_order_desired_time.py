# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20151112_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='desired_time',
        ),
    ]
