from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion.admin import VersionAdmin


@admin.register(Thumbnail)
class ThumbnailAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'image', 'uuid')


@admin.register(Capture)
class CaptureAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'thumbnail')


@admin.register(Item)
class ItemAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description', 'uuid')
    filter_horizontal = ('capture',)
