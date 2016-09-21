#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import View

from bricksa.apps.newsletter.models import Subscriber


class NewsletterView(View):
    def post(self, request):
        source = request.POST.get('source')
        email = request.POST.get('email')
        if email:
            try:
                subscriber = Subscriber.objects.get(
                    email=email,
                    source=source
                )
            except Subscriber.DoesNotExist:
                subscriber = Subscriber.objects.get(
                    email=email,
                    source=source
                )
                subscriber.save()
        return HttpResponse('Yeah')
