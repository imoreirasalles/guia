from django.contrib import admin
from .models import *
from reversion_compare.admin import CompareVersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class LocationResource(resources.ModelResource):

    class Meta:
        model = Location


@admin.register(Location)
class LocationAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id_auto_series', 'slug',)
    resource_class = LocationResource
    list_filter = ('country', 'state', 'city')
    list_display = ('id_auto_series', 'title', 'country', 'state', 'city', 'street')
    search_fields = ['__all__']
