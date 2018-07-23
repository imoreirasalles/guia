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
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CaptureResource(resources.ModelResource):

    class Meta:
        model = Capture


@admin.register(Capture)
class CaptureAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id_auto_series', 'slug',)
    resource_class = CaptureResource
    list_display = ('id_auto_series', 'uuid', 'title', 'image')
    search_fields = ['__all__']


class ItemResource(resources.ModelResource):

    class Meta:
        model = Item


@admin.register(Item)
class ItemAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id_auto_series', 'slug',)
    resource_class = ItemResource
    list_display = ('id_auto_series', 'uuid', 'title', 'description')
    search_fields = ['__all__']
    filter_horizontal = ('capture',)
