# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='full_name',
            new_name='client_name',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='phone_number',
            new_name='contact_number',
        ),
    ]
