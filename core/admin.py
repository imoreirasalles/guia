from django.contrib import admin
from django import forms
from .models import *
from mptt.models import MPTTModel, TreeForeignKey

# Froala WYSWYG editor https://github.com/froala/django-froala-editor
from froala_editor.widgets import FroalaEditor

# From postgres
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

# From Django Admin Hstore widget
from django_admin_hstore_widget.forms import HStoreFormField


admin.site.register(Thumbnail)
# admin.site.register(Person)


class PersonAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=FroalaEditor)
    full_text = forms.CharField(widget=FroalaEditor)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm


class CollectionAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=FroalaEditor)

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm
    # formfield_overrides = {
    #     fields.JSONField: {'widget': JSONEditorWidget},
    # }


# @admin.register(Collection)
# class Collection(admin.ModelAdmin):
#     formfield_overrides = {
#         fields.JSONField: {'widget': JSONEditorWidget},
#     }
