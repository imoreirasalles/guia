from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin


@admin.register(Location)
class LocationAdmin(VersionAdmin, admin.ModelAdmin):
    list_filter = ('country', 'state', 'city')
    list_display = ('id', 'title', 'country', 'state', 'city')
    search_fields = ['id', 'title', 'country', 'state', 'city', 'neighborhood', 'street', 'postal_code']
