#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View

from bricksa.apps.newsletter.models import Subscriber
from bricksa.apps.projects.models import Project, Brochure, ProjectPhoto


class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    model = Project

    def get_queryset(self,):
        arg = self.request.GET.get('u')
        if arg:
            queryset = Project.objects.filter(project_type=arg).order_by('order')
        else:
            queryset = Project.objects.all().order_by('order')
        return queryset


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    model = Project
    slug_url_kwarg = 'slug'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        project = kwargs.get('object')
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['photos'] = ProjectPhoto.objects.filter(project=project)
        return context


class DownloadFileView(View):
    def get(self, request, id):
        brochure = Brochure.objects.get(id=id)
        ext = brochure.file.name.split('.')[-1]
        filename = '%s.%s' % (brochure.project.name, ext)
        response = HttpResponse(
            brochure.file,
            content_type='application/force-download'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
