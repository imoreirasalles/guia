# Core django imports
from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
## Third part imports ##
# Froala WYSWYG editor https://github.com/froala/django-froala-editor
from froala_editor.widgets import FroalaEditor


class PersonAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=FroalaEditor)
    full_text = forms.CharField(widget=FroalaEditor)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    form = PersonAdminForm
