from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
# Froala WYSWYG editor https://github.com/froala/django-froala-editor
from froala_editor.widgets import FroalaEditor


admin.site.register(AccessCondition)


class DescriptionLevelAdminForm(forms.ModelForm):
    class Meta:
       model = DescriptionLevel
       fields = '__all__'
       verbose_name=_('Description Level')
       verbose_name_plural=_('Description Levels')
       labels = {
        'created': _('Created in'),
        'title': _('Title'),
        'description': _('Description'),
       }
       help_texts = {
        'created': _('Example of help text... '),
        'title': _('Example of help text... '),
        'description': _('Example of help text... '),
       }


@admin.register(DescriptionLevel)
class DescriptionLevelAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')
    form = DescriptionLevelAdminForm


class AggregationTypeAdminForm(forms.ModelForm):
    class Meta:
       model = AggregationType
       fields = '__all__'
       verbose_name=_('Aggregation Type')
       verbose_name_plural=_('Aggregations Type')
       labels = {
        'created': _('Created in'),
        'title': _('Title'),
        'description': _('Description'),
       }
       help_texts = {
        'created': _('Example of help text... '),
        'title': _('Example of help text... '),
        'description': _('Example of help text... '),
       }


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
    abstract = forms.CharField(widget=FroalaEditor, label='Resumo')

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    form = CollectionAdminForm
