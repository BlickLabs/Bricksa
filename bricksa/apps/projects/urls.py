#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^proyectos/$',
        view=views.ProjectListView.as_view(),
        name='project_list'),

    url(regex='^proyectos/(?P<id>.*)/$',
        view=views.ProjectDetailView.as_view(),
        name='project_detail'),

    url(regex='^brochure/(?P<id>.*)/$',
        view=views.DownloadFileView.as_view(),
        name='project_brochure'),
]