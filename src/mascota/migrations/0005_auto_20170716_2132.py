# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_auto_20170716_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.SmallIntegerField(max_length=2),
        ),
    ]
