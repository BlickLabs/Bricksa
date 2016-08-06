# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_brochure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectbanner',
            name='name',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[(b'departament', 'Departament'), (b'office', 'Office'), (b'house - room', 'House - Room')], max_length=30, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[(b'sale', 'Sale'), (b'pre-sale', 'Pre-sale'), (b'sold', 'Sold'), (b'in construction', 'In construction'), (b'finished', 'Finished')], max_length=30, verbose_name='Status'),
        ),
    ]
