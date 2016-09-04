#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from bricksa.apps.projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Project

    def clean_video(self):
        cleaned_data = super(ProjectForm, self).clean()
        video = cleaned_data.get('video')
        try:
            arg = video.split('=')[1]
        except:
            raise forms.ValidationError('Inserte un link de la forma https://www.youtube.com/watch?v=IVx6ZlksMJw')
        video_embedded = 'https://www.youtube.com/embed/%s' % arg
        return video_embedded