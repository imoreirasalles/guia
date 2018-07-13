from django.contrib import admin
from .models import *
from reversion_compare.admin import CompareVersionAdmin


@admin.register(Location)
class LocationAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_filter = ('country', 'state', 'city')
    list_display = ('id_auto_series', 'title', 'country', 'state', 'city', 'street')
    search_fields = ['__all__']
