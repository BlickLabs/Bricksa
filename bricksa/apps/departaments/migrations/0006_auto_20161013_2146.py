# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-13 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departaments', '0005_auto_20161011_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departament',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project'),
        ),
    ]
