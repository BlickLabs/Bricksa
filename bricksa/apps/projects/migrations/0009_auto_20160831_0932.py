# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-31 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160829_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Departament', 'Departament'), ('Office', 'Office'), ('House - Room', 'House - Room'), ('commercial', 'Commercial'), ('Fractionation', 'Fractionation')], max_length=30, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Current projects', 'Current projects'), ('Completed projects', 'Completed projects')], max_length=30, verbose_name='Project type'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Pre-sale', 'Pre-sale'), ('Sold', 'Sold'), ('In construction', 'In construction'), ('Finished', 'Finished')], max_length=30, verbose_name='Status'),
        ),
    ]
