from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ContainerResource(resources.ModelResource):

    class Meta:
        model = Container


@admin.register(Container)
class ContainerAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id_auto_series', 'slug',)
    resource_class = ContainerResource
    list_display = ('get_date_created', 'id_auto_series', 'id_human', 'uuid', 'title', 'description', 'description_level',)
    filter_horizontal = ('items', 'container_child')
    search_fields = ['__all__']


class CollectionResource(resources.ModelResource):

    class Meta:
        model = Collection


class CollectionAdminForm(forms.ModelForm):
    id_old = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Old IDs'))
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Text'))
    dimensions = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Dimensions'))
    inventary_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Inventary Data'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Other Unstructured Data'))

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id_auto_series', 'slug',)
    resource_class = CollectionResource
    list_filter = ('aggregation_type', 'genre_tags', 'author', 'access_condition', 'access_local_status', 'access_online_status', 'location_generic', 'inventary_status', 'inventary_last_date', 'management_unit', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'management_unit', 'aggregation_type', 'title', 'description_level', 'access_condition', 'inventary_status', 'items_total')
    search_fields = ['__all__']
    filter_horizontal = ('thumbnail', 'author', 'container')
    form = CollectionAdminForm
