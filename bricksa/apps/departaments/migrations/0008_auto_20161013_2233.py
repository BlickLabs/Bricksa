# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-13 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departaments', '0007_auto_20161013_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departament',
            name='kitchen',
        ),
        migrations.AddField(
            model_name='departament',
            name='integral_kitchen',
            field=models.BooleanField(default=False, verbose_name='Integral kitchen'),
        ),
        migrations.AddField(
            model_name='departament',
            name='kitchen_cupboard',
            field=models.BooleanField(default=False, verbose_name='Cupboard kitchen'),
        ),
    ]
