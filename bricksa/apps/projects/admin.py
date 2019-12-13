#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from bricksa.apps.projects.forms import ProjectForm
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'order')
    list_filter = ('category', 'status', 'project_type')
    form = ProjectForm
    fieldsets = (
        (_('General Information'), {
            'fields': (
                'name', 'brief_description', 'project_type', 'category', 'building',
                'status', 'thumbnail_1', 'thumbnail_2', 'address'
           )
        }),
        (_('Detail Information'), {
            'fields': ('photo', 'tablet', 'mobile', 'logo', 'description', 'video','google_maps_link'
            )
        }),
        (_('Specific information'), {
            'fields': (
            'construction_m2', 'number_departaments', 'parking_places', 'guardhouse',
            'waiting_area', 'common_area', 'dumpster_area', 'roof_garden', 'about_image',
            'lobby', 'multiple_room', 'closed_circuit', 'undergroun_services', 'green_areas',
            'access_gate', 'concrete_paving', 'club_house', 'elevator', 'solar_panel', 'water_treatment_plant',
            'indoor_garden', 'car_ramp', 'warehouse', 'extra_1', 'extra_2', 'extra_3'
            )
        }),
    )
    list_editable = ('order',)
    show_full_result_count = True


@admin.register(models.ProjectAmenities)
class ProjectBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProjectBanner)
class ProjectBannerAdmin(admin.ModelAdmin):
    list_display = ('project', 'photo', 'order',)
    list_editable = ('order',)
    show_full_result_count = True


@admin.register(models.ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    list_display = ('project', 'preview')
    list_filter = ('project',)


@admin.register(models.Brochure)
class BrochureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SeoData)
class SeoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SocialNetworks)
class SocialNetworksAdmin(admin.ModelAdmin):
    pass
