# Core django imports
from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


class PersonAdminForm(forms.ModelForm):
    abstract = forms.CharField(required=False)
    full_text = forms.CharField(required=False)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('person_type', 'is_staff', 'is_partner', 'is_feature', 'gender', 'date_start', 'date_end')
    form = PersonAdminForm
