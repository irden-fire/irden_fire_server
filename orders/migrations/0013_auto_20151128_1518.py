# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20151127_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_data',
            field=models.ForeignKey(related_name='orders', blank=True, to='authentication.UserData', null=True),
        ),
    ]
