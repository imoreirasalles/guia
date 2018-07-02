# Core django imports
from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


class PersonAdminForm(forms.ModelForm):
    abstract = forms.CharField()
    full_text = forms.CharField()


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    form = PersonAdminForm
