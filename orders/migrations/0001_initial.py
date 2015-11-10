# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('contact_number', models.CharField(default=b'', max_length=100, blank=True)),
                ('email', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
    ]
