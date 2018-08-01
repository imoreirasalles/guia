from django.contrib import admin
from .models import *
from reversion_compare.admin import CompareVersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class LocationResource(resources.ModelResource):

    class Meta:
        model = Location
        fields = ('uuid', 'title', 'street', 'number', 'complement', 'neighborhood', 'state', 'city', 'country', 'postal_code', 'lat_and_long')
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Location)
class LocationAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = LocationResource
    list_filter = ('country', 'state', 'city')
    list_display = ('id_auto_series', 'title', 'country', 'state', 'city', 'street')
    search_fields = ['__all__']
