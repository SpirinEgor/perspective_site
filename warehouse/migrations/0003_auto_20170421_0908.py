# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20170421_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipe',
            name='length',
            field=models.FloatField(default=0, verbose_name='Длина трубы'),
        ),
    ]