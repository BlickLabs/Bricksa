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
    logo = models.ImageField(
        _('Logo'),
        blank=False,
        null=False,
        upload_to='project_logos'
    )
    photo = models.ImageField(
        _('Photo'),
        blank=False,
        null=False,
        upload_to='project_photos'
    )
    thumbnail_1 = models.ImageField(
        _('Thumbnail 1'),
        blank=False,
        null=False,
        upload_to='project_photos'
    )
    thumbnail_2 = models.ImageField(
        _('Thumbnail 2'),
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
            (_('Departament'),_('Departament')),
            (_('Office'),_('Office')),
            (_('House - Room'),_('House - Room')),
            (_('commercial'),_('Commercial')),
            (_('Fractionation'),_('Fractionation')),
        ),
        blank=False,
        null=False,
        max_length=30,
    )
    status = models.CharField(
        _('Status'),
        choices=(
            (_('Sale'), _('Sale')),
            (_('Pre-sale'), _('Pre-sale')),
            (_('Sold'), _('Sold')),
            (_('In construction'), _('In construction')),
            (_('Finished'), _('Finished')),
        ),
        blank=False,
        null=False,
        max_length=30,
    )
    project_type = models.CharField(
        _('Project type'),
        choices=(
            (_('Current projects'), _('Current projects')),
            (_('Completed projects'), _('Completed projects')),
        ),
        blank=False,
        null=False,
        max_length=30,
    )
    google_maps_link = models.URLField(
        blank=False,
        null=False,
    )
    video = models.URLField(
        _('Video'),
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
        _('M2 Construction'),
        max_length=50,
        blank=False,
        null=False,
    )
    number_departaments = models.IntegerField(
        _('Number of departaments'),
        blank=False,
        null=False,
    )
    parking_places = models.IntegerField(
        _('Parking places'),
        blank=False,
        null=False,
    )
    guardhouse = models.BooleanField(
        _('Guarhouse'),
        blank=False,
        null=False,
        default=False,
    )
    waiting_area = models.BooleanField(
        _('Waiting area'),
        blank=False,
        null=False,
        default=False,
    )
    common_area = models.BooleanField(
        _('Common area'),
        blank=False,
        null=False,
        default=False,
    )
    dumpster_area = models.BooleanField(
        _('Dumpster area'),
        blank=False,
        null=False,
        default=False,
    )
    roof_garden = models.BooleanField(
        _('Roof garden'),
        blank=False,
        null=False,
        default=False,
    )

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __unicode__(self):
        return self.name


class ProjectBanner(models.Model):
    project = models.OneToOneField(
        Project,
        verbose_name=_('Project')
    )
    photo = models.ImageField(
        _('Photo'),
        blank=False,
        null=False,
        upload_to='project_banner_photos'
    )
    description = models.TextField(
        _('Description'),
        max_length=40,
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

    def preview(self):
        return """
        <img src="%s" width='100px' />
        """ % self.photo.url

    preview.allow_tags = True

    class Meta:
        verbose_name = _('Project Photo')
        verbose_name_plural = _('Project Photos')

    def __unicode__(self):
        return self.project.name


class Brochure(models.Model):
    project = models.OneToOneField(
        Project,
        verbose_name=_('Project')
    )
    file = models.FileField(
        _('File'),
        blank=False,
        null=False,
        upload_to='project_brochures',
    )

    class Meta:
        verbose_name = _('Brochure')
        verbose_name_plural = _('Brochures')

    def __unicode__(self):
        return 'Brochure - %s' % self.project.name