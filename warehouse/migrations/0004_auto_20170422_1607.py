# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20170421_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipe',
            name='weight',
            field=models.FloatField(default=0, verbose_name='Вес'),
        ),
        migrations.RemoveField(
            model_name='pipe',
            name='count',
        ),
        migrations.AlterUniqueTogether(
            name='pipe',
            unique_together=set([('GOST', 'material', 'wall_thickness', 'size', 'length', 'weight')]),
        ),
    ]
