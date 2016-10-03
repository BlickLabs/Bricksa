# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-02 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departaments', '0002_auto_20161002_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departament',
            name='bedrooms_with_closet',
            field=models.CharField(default=0, max_length=50, verbose_name='Bedrooms with closet'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='bedrooms_with_dress',
            field=models.CharField(default=0, max_length=50, verbose_name='Bedrooms with dress'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='complete_bathrooms',
            field=models.CharField(default=0, max_length=50, verbose_name='Complete bathrooms'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='dinning_room',
            field=models.BooleanField(default=False, verbose_name='Dinning room'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='half_bathrooms',
            field=models.CharField(default=0, max_length=50, verbose_name='Half bathrooms'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='kitchen',
            field=models.BooleanField(default=False, verbose_name='Kitchen'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='linen_closet',
            field=models.BooleanField(default=False, max_length=50, verbose_name='Linen closet'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='living_room',
            field=models.BooleanField(default=False, verbose_name='Living room'),
        ),
    ]