#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from bricksa.apps.projects.models import Project


class Office(models.Model):
    project = models.OneToOneField(
        Project,
        verbose_name=_('Project')
    )
    office_floors = models.IntegerField(
        _('Office floors'),
        blank=False,
        null=False,
        default=0
    )
    bathrooms_per_level = models.IntegerField(
        _('Bathrooms per level'),
        blank=False,
        null=False,
        default=0
    )
    elevator = models.BooleanField(
        _('Elevator'),
        blank=False,
        null=False,
        default=False
    )

    class Meta:
        verbose_name = _('Ofice')
        verbose_name_plural = _('Offices')

    def __unicode__(self):
        return 'Office - %s' % self.project.name