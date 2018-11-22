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


class PublicationTypeResource(resources.ModelResource):

    class Meta:
        model = PublicationType


@admin.register(PublicationType)
class PublicationTypeAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = PublicationTypeResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class PublicationAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))
    dimension = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Dimensions'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Other Unstructured Data'))

    class Meta:
        model = Publication
        fields = '__all__'


class PublicationResource(resources.ModelResource):

    class Meta:
        model = Publication
        fields = ('uuid', 'title', 'id_human', 'type', 'abstract', 'full_text', 'date_released', )
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Publication)
class PublicationAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug', )
    resource_class = PublicationResource
    list_display = ('id_auto_series', 'uuid', 'title', 'date_released', 'is_draft')
    search_fields = ['title']
    filter_horizontal = ('author', 'publisher', 'capture')
    form = PublicationAdminForm
