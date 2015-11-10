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
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('cost', models.DecimalField(max_digits=5, decimal_places=2, blank=True)),
                ('duration', models.CharField(default=b'', max_length=100, blank=True)),
                ('how_many_participants', models.IntegerField(max_length=2, blank=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('cost',),
            },
        ),
    ]
