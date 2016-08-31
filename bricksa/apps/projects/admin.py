#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')
    list_filter = ('category', 'status', 'project_type')
    fieldsets = (
        (_('Thumbnail information'), {
            'fields': (
                'name', 'photo', 'logo', 'brief_description', 'category',
                'status', 'thumbnail_1', 'thumbnail_2'
           )
        }),
        (_('Detail Information'), {
            'fields': (
                'description', 'google_maps_link', 'video', 'ground_m2',
                'construction_m2', 'project_type'
            )
        }),
    )


@admin.register(models.ProjectBanner)
class ProjectBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    list_display = ('project', 'preview')
    list_filter = ('project',)


@admin.register(models.Brochure)
class BrochureAdmin(admin.ModelAdmin):
    pass
