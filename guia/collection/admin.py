from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from .models import Collection

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("label", "summary", "inventory_status", "contract_status", "insurance_status", "dimention_items", "published",)
    readonly_fields = ["created_at", "updated_at", "uuid", "slug", ]
    fieldsets = (
                (_('Basic information'),
                    {'fields':  (
                        ('label', 'published'),
                        ('summary')),
                    }),
                (_('Full description'),
                    {'fields': (
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
                        ('id_human'),
                        ('inventory_status', 'inventory_date'),
                        ('contract_status', 'contract_date'),
                        ('insurance_status', 'insurance_date')),
                    }),
    )