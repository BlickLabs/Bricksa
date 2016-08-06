#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=50,
        blank=False,
        null=False
    )
    photo = models.ImageField(
        _('Photo'),
        blank=False,
        null=False,
        upload_to='project_photos'
    )
    brief_description = models.TextField(
        _('Brief description'),
        max_length=140,
        blank=False,
        null=False,
    )
    description = models.TextField(
        _('Description'),
        max_length=140,
        blank=False,
        null=False,
    )
    category = models.CharField(
        _('Category'),
        choices=(
            (('departament'),_('Departamento')),
            (('office'),_('Office')),
            (('house - room'),_('House - Room')),
        ),
        blank=False,
        null=False,
        max_length=30,
    )
    status = models.CharField(
        _('Category'),
        choices=(
            (('sale'), _('Sale')),
            (('pre-sale'), _('Pre-sale')),
            (('sold'), _('Sold')),
            (('in construction'), _('In construction')),
            (('finished'), _('Finished')),
        ),
        blank=False,
        null=False,
        max_length=30,
    )
    google_maps_link = models.URLField(
        blank=False,
        null=False,
    )
    ground_m2 = models.CharField(
        _('M2 Ground'),
        max_length=50,
        blank=False,
        null=False,
    )
    construction_m2 = models.CharField(
        _('M2 Ground'),
        max_length=50,
        blank=False,
        null=False,
    )
    video = models.URLField(
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __unicode__(self):
        return self.name


class ProjectBanner(models.Model):
    project = models.ForeignKey(
        Project,
        verbose_name=_('Project')
    )
    name = models.CharField(
        _('Name'),
        max_length=50,
        blank=False,
        null=False
    )
    photo = models.ImageField(
        _('Photo'),
        blank=False,
        null=False,
        upload_to='project_banner_photos'
    )
    description = models.TextField(
        _('Description'),
        max_length=140,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Project Banner')
        verbose_name_plural = _('Project Banners')

    def __unicode__(self):
        return self.project.name


class ProjectPhoto(models.Model):
    project = models.ForeignKey(
        Project,
        verbose_name=_('Project')
    )
    photo = models.ImageField(
        _('Photo'),
        blank=False,
        null=False,
        upload_to='project_banner_photos'
    )

    class Meta:
        verbose_name = _('Project Photo')
        verbose_name_plural = _('Project Photos')

    def __unicode__(self):
        return self.project.name
