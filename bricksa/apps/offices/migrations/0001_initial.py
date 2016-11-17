# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-17 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0024_auto_20161117_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_floors', models.IntegerField(default=0, verbose_name='Office floors')),
                ('bathrooms_per_level', models.IntegerField(default=0, verbose_name='Bathrooms per level')),
                ('elevator', models.IntegerField(default=0, verbose_name='Elevator')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project')),
            ],
        ),
    ]
