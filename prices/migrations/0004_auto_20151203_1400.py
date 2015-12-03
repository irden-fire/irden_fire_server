# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_pricedescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricedescription',
            name='price',
        ),
        migrations.AddField(
            model_name='price',
            name='description_l18n',
            field=models.OneToOneField(related_name='price', null=True, blank=True, to='prices.PriceDescription'),
        ),
        migrations.AddField(
            model_name='pricedescription',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
