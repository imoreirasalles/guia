from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from .models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("label", "summary", "inventory_status", "contract_status",
                    "insurance_status", "dimention_items", "published",)
    list_filter = ('aggregation_type',)
    readonly_fields = ["created_at", "updated_at", "uuid", "slug", ]
    filter_horizontal = ('aggregation_type',)
    fieldsets = (
                (_('Basic information'),
                    {'fields':  (
                        ('label', 'published'),
                        ('summary')),
                     }),
                (_('Full description'),
                    {'fields': (
                        ('id_human'),
                        ('aggregation_type'),
                        ('start_date', 'end_date'),
                        ('article'))
                     }),
                (_('Progress Bar'),
                    {'fields': (
                        ('progressbar_work', 'progressbar_online')),
                     }),
                (_('Management'),
                    {'fields': (
                        ('inventory_status', 'inventory_start_date', 'inventory_end_date'),
                        ('contract_status', 'contract_start_date', 'contract_end_date'),
                        ('insurance_status', 'insurance_start_date', 'insurance_end_date')),
                     }),
    )
