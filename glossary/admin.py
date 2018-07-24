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


class AccessConditionResource(resources.ModelResource):

    class Meta:
        model = AccessCondition


@admin.register(AccessCondition)
class AccessConditionAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = AccessConditionResource
    list_display = ('id_auto_series', 'title', 'title_long', 'description')
    search_fields = ['__all__']


class DescriptionLevelResource(resources.ModelResource):

    class Meta:
        model = DescriptionLevel


@admin.register(DescriptionLevel)
class DescriptionLevelAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = DescriptionLevelResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class AggregationTypeResource(resources.ModelResource):

    class Meta:
        model = AggregationType


@admin.register(AggregationType)
class AggregationTypeAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = AggregationTypeResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class GenreTagResource(resources.ModelResource):

    class Meta:
        model = GenreTag


@admin.register(GenreTag)
class GenreTagAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id_auto_series', 'slug',)
    resource_class = GenreTagResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']
