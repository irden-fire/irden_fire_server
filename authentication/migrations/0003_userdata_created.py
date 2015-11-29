# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20151125_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 22, 29, 56, 67140, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
