#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView

from bricksa.apps.projects.models import Project


class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    model = Project

    def get_queryset(self,):
        arg = self.request.GET.get('u')
        print arg
        if arg:
            queryset = Project.objects.filter(project_type=arg)
        else:
            queryset = super(ProjectListView, self).get_queryset()
        return queryset


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    model = Project
    pk_url_kwarg = 'id'
    context_object_name = 'project'
