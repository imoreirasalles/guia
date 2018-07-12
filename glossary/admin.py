from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


admin.site.register(AccessCondition)


@admin.register(DescriptionLevel)
class DescriptionLevelAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(AggregationType)
class AggregationTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(GenreTag)
class GenreTagAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')
