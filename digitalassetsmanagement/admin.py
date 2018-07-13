from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin


@admin.register(Thumbnail)
class ThumbnailAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'uuid', 'title', 'image')
    search_fields = ['__all__']


@admin.register(Capture)
class CaptureAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'uuid', 'title', 'thumbnail')
    search_fields = ['__all__']


@admin.register(Item)
class ItemAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'uuid', 'title', 'description')
    search_fields = ['__all__']
    filter_horizontal = ('capture',)
