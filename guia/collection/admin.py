from django.contrib import admin

from .models import Collection

# Register your models here.


class CollectionAdmin(admin.ModelAdmin):
    list_display = ("label", "summary", "uuid", "published",)
    readonly_fields = ["created_at", "updated_at", "uuid", "slug", ]


admin.site.register(Collection, CollectionAdmin)
