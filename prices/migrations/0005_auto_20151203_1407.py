# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0004_auto_20151203_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='description_l18n',
        ),
        migrations.AddField(
            model_name='pricedescription',
            name='price',
            field=models.ForeignKey(related_name='description_l18n', blank=True, to='prices.Price', null=True),
        ),
    ]
