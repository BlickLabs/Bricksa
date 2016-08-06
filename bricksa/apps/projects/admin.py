#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')
    list_filter = ('category', 'status')


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
