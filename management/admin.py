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


class ManagementUnitResource(resources.ModelResource):

    class Meta:
        model = ManagementUnit


@admin.register(ManagementUnit)
class ManagementUnitAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ManagementUnitResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class ProcedureResource(resources.ModelResource):

    class Meta:
        model = Procedure


@admin.register(Procedure)
class ProcedureAdmin(CompareVersionAdmin, admin.ModelAdmin):
    resource_class = ProcedureResource
    list_display = ('id_auto_series', 'title', 'slug')
    search_fields = ['__all__']


class AcquisitionMethodResource(resources.ModelResource):

    class Meta:
        model = AcquisitionMethod


@admin.register(AcquisitionMethod)
class AcquisitionMethodAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AcquisitionMethodResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class AcquisitionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Text'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Other Unstructured Data'))

    class Meta:
        model = Acquisition
        fields = '__all__'


class AcquisitionResource(resources.ModelResource):

    class Meta:
        model = Acquisition


@admin.register(Acquisition)
class AcquisitionAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AcquisitionResource
    list_filter = ('method', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'title', 'method', 'date_start', 'date_end')
    search_fields = ['__all__']
    filter_horizontal = ('source', 'dealer', )
    form = AcquisitionAdminForm
