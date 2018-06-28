from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
## Third part imports ##
# Froala WYSWYG editor https://github.com/froala/django-froala-editor
from froala_editor.widgets import FroalaEditor


admin.site.register(AccessCondition)


@admin.register(DescriptionLevel)
class DescriptionLevelAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(AggregationType)
class AggregationTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(GenreTag)
class GenreTag(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(Thumbnail)
class Thumbnail(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'image', 'uuid')


@admin.register(Item)
class Item(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description', 'uuid')


@admin.register(Sets)
class Sets(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'abstract', 'description_level', 'uuid', 'sets_child')


class CollectionAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=FroalaEditor)

    class Meta:
       model = Collection
       fields = '__all__'
       labels = {
        'abstract': ('Resumo')
       }
       help_texts = {
        'abstract': ('Resumo')
       }
       verbose_name = {
        'abstract': ('Resumo')
       }


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    form = CollectionAdminForm
