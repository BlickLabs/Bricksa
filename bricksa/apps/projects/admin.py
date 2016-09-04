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
        (_('General Information'), {
            'fields': (
                'name', 'brief_description', 'project_type', 'category',
                'status', 'thumbnail_1', 'thumbnail_2'
           )
        }),
        (_('Detail Information'), {
            'fields': ('photo', 'logo', 'description', 'video','google_maps_link'
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
