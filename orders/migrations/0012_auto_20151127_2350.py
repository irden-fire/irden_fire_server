# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20151125_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_data',
            field=models.ForeignKey(blank=True, to='authentication.UserData', null=True),
        ),
    ]
