from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
## Third part imports ##
# Froala WYSWYG editor https://github.com/froala/django-froala-editor
from froala_editor.widgets import FroalaEditor


admin.site.register(Thumbnail)

class CollectionAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=FroalaEditor)

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm
