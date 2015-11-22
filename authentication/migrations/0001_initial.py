# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('phone_number', models.CharField(default=b'', max_length=100, blank=True)),
                ('email', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
    ]
