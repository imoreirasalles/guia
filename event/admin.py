from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'created', 'title', 'description')
    search_fields = ['id', 'created', 'title', 'description']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'created', 'title', 'date_start', 'date_end', 'type', 'location')
    search_fields = ['id', 'created', 'title', 'date_start', 'date_end', 'type__title', 'location__title']
