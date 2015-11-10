# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='how_many_participants',
            field=models.IntegerField(blank=True),
        ),
    ]
