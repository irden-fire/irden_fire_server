# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20151128_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
