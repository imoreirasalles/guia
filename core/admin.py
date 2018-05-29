from django.contrib import admin
from django import forms
from .models import *

# From postgres
from django.contrib.postgres import fields

# From Django Admin Hstore widget
from django_admin_hstore_widget.forms import HStoreFormField


admin.site.register(Thumbnail)
admin.site.register(Person)

class CollectionAdminForm(forms.ModelForm):
    id_old = HStoreFormField()

    class Meta:
       model = Collection
       exclude = ()

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm

# @admin.register(Collection)
# class Collection(admin.ModelAdmin):
#     formfield_overrides = {
#         fields.JSONField: {'widget': JSONEditorWidget},
#     }
