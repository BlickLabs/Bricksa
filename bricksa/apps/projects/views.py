#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import ListView

from bricksa.apps.projects.models import Project


class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'project'