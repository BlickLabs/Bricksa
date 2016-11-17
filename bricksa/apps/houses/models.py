#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from bricksa.apps.projects.models import Project


class House(models.Model):
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
    beforedinning_room = models.BooleanField(
        _('Before dinning room'),
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
    study = models.BooleanField(
        _('Study'),
        blank=False,
        null=False,
        default=False
    )
    bar = models.BooleanField(
        _('Bar'),
        blank=False,
        null=False,
        default=False
    )
    cellar = models.BooleanField(
        _('Cellar'),
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
    balcony = models.BooleanField(
        _('Balcony'),
        blank=False,
        null=False,
        default=False
    )
    deck = models.BooleanField(
        _('Deck'),
        blank=False,
        null=False,
        default=False
    )
    deck_with_gas_fireplace = models.BooleanField(
        _('Deck with gas fireplacek'),
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
    swimming_pool = models.BooleanField(
        _('Swimming Pool'),
        blank=False,
        null=False,
        default=False
    )
    jacuzzi = models.BooleanField(
        _('Jacuzzi'),
        blank=False,
        null=False,
        default=False
    )
    bathroom_with_tub = models.BooleanField(
        _('Bathroom with tub'),
        blank=False,
        null=False,
        default=False
    )
    game_room = models.BooleanField(
        _('Game room'),
        blank=False,
        null=False,
        default=False
    )
    guest_room = models.BooleanField(
        _('Guest room'),
        blank=False,
        null=False,
        default=False
    )
    guest_bathroom = models.BooleanField(
        _('Guest bathroom'),
        blank=False,
        null=False,
        default=False
    )
    interior_garden = models.BooleanField(
        _('Interior garden'),
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
    room_service = models.BooleanField(
        _('Room service'),
        blank=False,
        null=False,
        default=False
    )

    floor_heating_system = models.BooleanField(
        _('Floor heating system'),
        blank=False,
        null=False,
        default=False
    )
    warehouse = models.BooleanField(
        _('Warehouse'),
        blank=False,
        null=False,
        default=False
    )
    water_glass = models.IntegerField(
        _('Water glass'),
        blank=False,
        null=False,
        default=0
    )

    class Meta:
        verbose_name = _('House')
        verbose_name_plural = _('Houses')

    def __unicode__(self):
        return 'House - %s' % self.project.name