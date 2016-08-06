#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProjectBanner)
class ProjectBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    pass
