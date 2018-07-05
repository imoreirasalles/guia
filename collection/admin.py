from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


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


@admin.register(Container)
class Container(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description', 'description_level', 'uuid')


class CollectionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        widget=CKEditorWidget(),
        label='Descrição Completa')

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'aggregation_type', 'date_start', 'date_end', 'items_total')
    search_fields = ['uuid', 'id', 'id_old', 'title', 'author__nickname']
    form = CollectionAdminForm
