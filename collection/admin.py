from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description', 'description_level', 'uuid')
    filter_horizontal = ('items', 'container_child')


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
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('aggregation_type', 'genre_tags', 'author', 'access_condition', 'access_local_status', 'access_online_status', 'location_generic', 'inventary_status', 'inventary_last_date', 'management_unit', 'date_start', 'date_end')
    list_display = ('id', 'management_unit', 'aggregation_type', 'title', 'description_level', 'access_condition', 'inventary_status', 'items_total')
    search_fields = ['uuid', 'id', 'id_old', 'title', 'author__nickname']
    filter_horizontal = ('thumbnail', 'author', 'container', 'items')
    form = CollectionAdminForm
