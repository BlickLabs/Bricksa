#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^subscribe/$',
        view=views.NewsletterView.as_view(),
        name='suscribe'),
]