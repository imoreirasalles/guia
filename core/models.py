from django.db import models
from django.contrib import admin


@admin.register(Collection)
class Collection(VersionAdmin):
    uuid
