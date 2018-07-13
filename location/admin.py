from django.contrib import admin
from .models import *
from reversion_compare.admin import CompareVersionAdmin


@admin.register(Location)
class LocationAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_filter = ('country', 'state', 'city')
    list_display = ('id', 'title', 'country', 'state', 'city')
    search_fields = ['id', 'title', 'country', 'state', 'city', 'neighborhood', 'street', 'postal_code']
