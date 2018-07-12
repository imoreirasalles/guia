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
class GenreTagAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'description')


@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'image', 'uuid')


@admin.register(Capture)
class CaptureAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('title', 'thumbnail')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description', 'uuid')
    filter_horizontal = ('capture',)


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description', 'description_level', 'uuid')
    filter_horizontal = ('items', 'container_child')


class CollectionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label='Descrição Completa')

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('aggregation_type', 'genre_tags', 'author', 'access_condition', 'access_local_status', 'access_online_status', 'location_generic', 'inventary_status', 'inventary_last_date', 'management_unit', 'date_start', 'date_end')
    list_display = ('id', 'management_unit', 'aggregation_type', 'title', 'description_level', 'access_condition', 'inventary_status', 'items_total')
    search_fields = ['uuid', 'id', 'id_old', 'title', 'author__nickname']
    filter_horizontal = ('thumbnail', 'author', 'container', 'items')
    form = CollectionAdminForm
