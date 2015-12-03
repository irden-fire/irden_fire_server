# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20151105_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceDescription',
            fields=[
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('description', models.TextField()),
                ('language', models.CharField(default=b'ru', max_length=4, blank=True)),
                ('price', models.OneToOneField(related_name='description_l18n', primary_key=True, serialize=False, to='prices.Price')),
            ],
        ),
    ]
