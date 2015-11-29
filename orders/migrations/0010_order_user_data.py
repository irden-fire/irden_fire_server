# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20151125_1459'),
        ('orders', '0009_remove_order_desired_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_data',
            field=models.ForeignKey(related_name='user_data', default=0, to='authentication.UserData'),
        ),
    ]
