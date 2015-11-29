# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_data',
            field=models.ForeignKey(default=0, to='authentication.UserData'),
        ),
    ]
