# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-17 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_projectbanner_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='access_gate',
            field=models.BooleanField(default=False, verbose_name='Access gate'),
        ),
        migrations.AddField(
            model_name='project',
            name='closed_circuit',
            field=models.BooleanField(default=False, verbose_name='Closed circuit'),
        ),
        migrations.AddField(
            model_name='project',
            name='club_house',
            field=models.BooleanField(default=False, verbose_name='Concrete paving'),
        ),
        migrations.AddField(
            model_name='project',
            name='concrete_paving',
            field=models.BooleanField(default=False, verbose_name='Concrete paving'),
        ),
        migrations.AddField(
            model_name='project',
            name='green_areas',
            field=models.IntegerField(default=0, verbose_name='Green areas'),
        ),
        migrations.AddField(
            model_name='project',
            name='lobby',
            field=models.BooleanField(default=False, verbose_name='Lobby'),
        ),
        migrations.AddField(
            model_name='project',
            name='multiple_room',
            field=models.BooleanField(default=False, verbose_name='Multipurpose room'),
        ),
        migrations.AddField(
            model_name='project',
            name='undergroun_services',
            field=models.BooleanField(default=False, verbose_name='All services underground'),
        ),
    ]