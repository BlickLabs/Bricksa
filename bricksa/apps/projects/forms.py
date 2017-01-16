#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.text import slugify

from bricksa.apps.projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Project

    def clean_video(self):
        cleaned_data = super(ProjectForm, self).clean()
        video = cleaned_data.get('video')
        if 'embed' in video:
            video_embedded = video
        elif video == '':
            video_embedded = ''
        else:
            try:
                arg = video.split('=')[1]
                video_embedded = 'https://www.youtube.com/embed/%s' % arg
            except:
                raise forms.ValidationError('Inserte un link de la forma https://www.youtube.com/watch?v=IVx6ZlksMJw')
        return video_embedded

    def save(self, commit=True):
        m = super(ProjectForm, self).save(commit=False)
        m.slug = slugify(m.name)
        if commit:
            m.save()
        return m