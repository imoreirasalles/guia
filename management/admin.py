from django.contrib import admin
from .models import *

@admin.register(ManagementUnit)
class ManagementUnitAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description')


@admin.register(AcquisitionMethod)
class AcquisitionMethodAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description')


@admin.register(Acquisition)
class AcquisitionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('method', 'date_start', 'date_end')
    list_display = ('uuid', 'title', 'method', 'date_start', 'date_end')
    search_fields = ('uuid', 'title')
    filter_horizontal = ('source', 'dealer', )
