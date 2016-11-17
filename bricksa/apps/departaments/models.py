#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from bricksa.apps.projects.models import Project


class Departament(models.Model):
    project = models.OneToOneField(
        Project,
        verbose_name=_('Project')
    )
    bedrooms_with_dress = models.IntegerField(
        _('Bedrooms with dress'),
        blank=False,
        null=False,
        default=0
    )
    bedrooms_with_closet = models.IntegerField(
        _('Bedrooms with closet'),
        blank=False,
        null=False,
        default=0
    )
    complete_bathrooms = models.IntegerField(
        _('Complete bathrooms'),
        blank=False,
        null=False,
        default=0
    )
    half_bathrooms = models.IntegerField(
        _('Half bathrooms'),
        blank=False,
        null=False,
        default=0
    )
    living_room = models.BooleanField(
        _('Living room'),
        blank=False,
        null=False,
        default=False
    )
    dinning_room = models.BooleanField(
        _('Dinning room'),
        blank=False,
        null=False,
        default=False
    )
    integral_kitchen = models.BooleanField(
        _('Integral kitchen'),
        blank=False,
        null=False,
        default=False
    )
    kitchen_cupboard = models.BooleanField(
        _('Cupboard kitchen'),
        blank=False,
        null=False,
        default=False
    )
    linen_closet = models.BooleanField(
        _('Linen closet'),
        max_length=50,
        blank=False,
        null=False,
        default=False
    )
    service_yard = models.BooleanField(
        _('Service yard'),
        blank=False,
        null=False,
        default=False
    )
    garden = models.BooleanField(
        _('Garden'),
        blank=False,
        null=False,
        default=False
    )
    terrace = models.BooleanField(
        _('Terrace'),
        blank=False,
        null=False,
        default=False
    )
    tv_room = models.BooleanField(
        _('TV Room'),
        blank=False,
        null=False,
        default=False
    )
    study = models.BooleanField(
        _('Study'),
        blank=False,
        null=False,
        default=False
    )
    room_service = models.BooleanField(
        _('Room service'),
        blank=False,
        null=False,
        default=False
    )

    class Meta:
        verbose_name = _('Departament')
        verbose_name_plural = _('Departaments')

    def __unicode__(self):
        return 'Departament - %s' % self.project.name