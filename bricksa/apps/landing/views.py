#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, View

from bricksa.apps.projects.models import ProjectBanner
from bricksa.core.utils import send_email


class HomepageView(View):
    def get(self, request):
        banners = ProjectBanner.objects.all()
        ctx = {
            'banners': banners
        }
        return TemplateResponse(request, 'landing/index.html', ctx)

class ServicesView(TemplateView):
    template_name = 'landing/services.html'

class AboutUsView(TemplateView):
    template_name = 'landing/about.html'


class ContactEmailView(View):
    def get(self, request):
        return TemplateResponse(request, 'landing/contact.html')

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')

        ctx = {
            'sender': name,
            'email': email,
            'message': message
        }

        send_email(
            subject='email/subjects/contact.txt',
            body='email/contact.html',
            from_email="Bricksa - Contacto <postmaster@%s>" % (
                settings.MAILGUN_SERVER_NAME
            ),
            to_email=[settings.DEFAULT_EMAIL_TO],
            context=ctx
        )


        return redirect(reverse('landing:success_contact'))


class SuccesEmailView(TemplateView):
    template_name = "landing/succes_contact.html"
