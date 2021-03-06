from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from . models import *
from person.models import Person
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ManagementUnitResource(resources.ModelResource):

    class Meta:
        model = ManagementUnit
        fields = ('uuid', 'title', 'description')
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(ManagementUnit)
class ManagementUnitAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = ManagementUnitResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class ProcedureResource(resources.ModelResource):

    class Meta:
        model = Procedure


@admin.register(Procedure)
class ProcedureAdmin(CompareVersionAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = ProcedureResource
    list_display = ('id_auto_series', 'title', 'slug')
    search_fields = ['__all__']


class AcquisitionMethodResource(resources.ModelResource):

    class Meta:
        model = AcquisitionMethod


@admin.register(AcquisitionMethod)
class AcquisitionMethodAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
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
class AcquisitionAdmin(CompareVersionAdmin, ImportExportModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = AcquisitionResource
    list_filter = ('method', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'title', 'method', 'date_start', 'date_end')
    search_fields = ['__all__']
    filter_horizontal = ('source', 'dealer', )
    form = AcquisitionAdminForm

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'source':
            kwargs["queryset"] = Person.objects.filter(is_feature=True)
        if db_field.name == 'dealer':
            kwargs["queryset"] = Person.objects.filter(is_staff=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
