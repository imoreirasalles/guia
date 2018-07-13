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


@admin.register(AccessCondition)
class AccessConditionAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'title_short', 'title_long', 'description')
    search_fields = ['__all__']


@admin.register(DescriptionLevel)
class DescriptionLevelAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


@admin.register(AggregationType)
class AggregationTypeAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


@admin.register(GenreTag)
class GenreTagAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']
