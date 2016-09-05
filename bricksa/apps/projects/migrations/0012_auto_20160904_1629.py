# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160904_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='common_area',
            field=models.BooleanField(default=False, verbose_name='Common area'),
        ),
        migrations.AddField(
            model_name='project',
            name='dumpster_area',
            field=models.BooleanField(default=False, verbose_name='Dumpster area'),
        ),
        migrations.AddField(
            model_name='project',
            name='guardhouse',
            field=models.BooleanField(default=False, verbose_name='Guarhouse'),
        ),
        migrations.AddField(
            model_name='project',
            name='number_departaments',
            field=models.IntegerField(default=10, verbose_name='Number of departaments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='parking_places',
            field=models.IntegerField(default=1, verbose_name='Parking places'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='roof_garden',
            field=models.BooleanField(default=False, verbose_name='Roof garden'),
        ),
        migrations.AddField(
            model_name='project',
            name='waiting_area',
            field=models.BooleanField(default=False, verbose_name='Waiting area'),
        ),
    ]