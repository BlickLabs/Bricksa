# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-02 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20160919_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectbanner',
            name='description',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='google_maps_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='number_departaments',
            field=models.IntegerField(default=0, verbose_name='Number of departaments'),
        ),
        migrations.AlterField(
            model_name='project',
            name='parking_places',
            field=models.IntegerField(default=0, verbose_name='Parking places'),
        ),
    ]