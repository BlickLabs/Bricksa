#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Departament)
class DepartamentAdmin(admin.ModelAdmin):
    pass