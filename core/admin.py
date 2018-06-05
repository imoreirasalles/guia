from django.contrib import admin
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

# From postgres
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

# From Django Admin Hstore widget
from django_admin_hstore_widget.forms import HStoreFormField


# admin.site.register(Thumbnail)
admin.site.register(Person)

@admin.register(Thumbnail)
class ThumbnailAdminForm(admin.ModelAdmin):
    class Meta:
        model = Thumbnail
        fields = ('title', 'image')
        labels = {
            'title': _('Title'),
        }
        help_texts = {
            'title': _('Title or subtitle about the image.'),
        }


class CollectionAdminForm(forms.ModelForm):
    id_old = HStoreFormField()

    class Meta:
       model = Collection
       exclude = ()

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

# @admin.register(Collection)
# class Collection(admin.ModelAdmin):
#     formfield_overrides = {
#         fields.JSONField: {'widget': JSONEditorWidget},
#     }
