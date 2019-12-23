from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from .models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("label", "summary", "inventory_status", "contract_status",
                    "insurance_status", "items_total", 'linear_meters', "published",)
    list_filter = ('aggregation_type', 'management_unit', 'acquisition_type',)
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
                        ('start_date', 'end_date'),
                        ('article'),
                        ('aggregation_type'))
                     }),
                (_('Dimentions'),
                    {'fields': (
                        ('items_total', 'linear_meters')),
                     }),
                (_('Progress Bar'),
                    {'fields': (
                        ('progress_technical', 'progress_online')),
                     }),
                (_('Management'),
                    {'fields': (
                        ('id_human', 'management_unit'),
                        ('acquisition_type'),
                        ('contract_status', 'contract_start_date', 'contract_end_date'),
                        ('inventory_status', 'inventory_start_date', 'inventory_end_date'),
                        ('insurance_status', 'insurance_start_date', 'insurance_end_date'),
                        ('private_notes',)),
                     }),
    )
