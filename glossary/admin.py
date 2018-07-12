from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from reversion.admin import VersionAdmin


@admin.register(AccessCondition)
class AccessConditionAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ('title_short', 'title_long', 'description')


@admin.register(DescriptionLevel)
class DescriptionLevelAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(AggregationType)
class AggregationTypeAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(GenreTag)
class GenreTagAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')
