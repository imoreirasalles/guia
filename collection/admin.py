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
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = ContainerResource
    list_display = ('get_date_created', 'id_auto_series', 'id_human', 'uuid', 'title', 'description', 'description_level',)
    filter_horizontal = ('items', 'container_child')
    search_fields = ['id_human', 'aggregation_type__title', 'description', 'items__title', 'description_level__title', 'container_child__title']


class CollectionResource(resources.ModelResource):

    class Meta:
        model = Collection


class CollectionAdminForm(forms.ModelForm):
    id_old = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=_('Old IDs'))
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Text'))
    dimensions = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=_('Dimensions'))
    inventary_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=_('Inventary Data'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=True),
        label=_('Other Unstructured Data'))

    def get_queryset(self):
        return Collection.objects.filter(author__is=True)

    class Meta:
       model = Collection
       fields = '__all__'


@admin.register(Collection)
class CollectionAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = CollectionResource
    list_filter = ('management_unit', 'aggregation_type', 'description_level', 'access_condition', 'genre_tags')
    list_display = ('id_human', 'management_unit', 'aggregation_type', 'title', 'description_level', 'access_condition', 'inventary_status', 'items_total')
    search_fields = ['id_human', 'id_old', 'abstract', 'full_text', 'description_level__title', 'aggregation_type__title', 'genre_tags__title', 'dimensions', 'date_start', 'date_start_caption', 'date_end', 'date_end_caption', 'capture__title', 'author__title', 'container__title', 'access_condition__title', 'location_generic__title', 'management_unit__title', 'other_data', ]
    filter_horizontal = ('capture', 'author', 'container')
    fieldsets = (
        (_('Indentification'), {
        'classes': ('wide','id_old_fix'),
        'fields': ( ('uuid', 'created'),
                    ('id_human', 'id_old'),
                    ('management_unit', 'aggregation_type'),
                    ('title', 'slug'),
                    ('capture'),
        ),}
        ),
        (_('Basic Infos'), {
        'fields': ( ('date_start', 'date_start_caption'),
                    ('date_end', 'date_end_caption'),
                    ('access_condition', 'description_level'),
                    ('genre_tags'),
                    ('abstract'),
        ),}
        ),
        (_('Location and Dimensions'), {
        'fields': ( ('location_generic', 'location_specific'),
                    ('dimensions'),
        ),}
        ),
        (_('Inventory and Patrimony'), {
        'fields': ( ('inventary_status', 'inventary_last_date'),
                    ('inventary_data'),
        ),}
        ),
        (_('Access'), {
        'fields': ( ('access_local_status', ),
                    ('access_online_status', 'access_link'),
        ),}
        ),
        (_('Processed Status'), {
        'fields': ( ('items_total', 'items_processed', 'items_online'),
        ),}
        ),

        (_('Description'), {
        'fields': ('full_text', 'container'),}
        ),
        (_('Other Infos'), {
        'fields': ('other_data',),
        }),
    )
    form = CollectionAdminForm
    class Media:
        css = {
             'all': ('css/guia.css',)
        }
