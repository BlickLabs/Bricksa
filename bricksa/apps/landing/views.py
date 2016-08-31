#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template.response import TemplateResponse
from django.views.generic import View


class HomepageView(View):
    def get(self, request):
        return TemplateResponse(request, 'landing/index.html')
