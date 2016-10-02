#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^$',
        view=views.HomepageView.as_view(),
        name='homepage'),

    url(regex=r'^servicios/$',
        view=views.ServicesView.as_view(),
        name='services'),

    url(regex=r'^nosotros/$',
        view=views.AboutUsView.as_view(),
        name='about'),

    url(regex=r'^contacto/$',
        view=views.ContactEmailView.as_view(),
        name='contact'),

    url(regex=r'^contacto/hecho/$',
        view=views.SuccesEmailView.as_view(),
        name='success_contact'),

]
