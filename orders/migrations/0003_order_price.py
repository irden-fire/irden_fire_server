# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20151105_1350'),
        ('orders', '0002_auto_20151106_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.ForeignKey(related_name='orders', default=0, to='prices.Price'),
        ),
    ]
