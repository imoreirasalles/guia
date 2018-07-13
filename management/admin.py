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


@admin.register(ManagementUnit)
class ManagementUnitAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


@admin.register(AcquisitionMethod)
class AcquisitionMethodAdmin(CompareVersionAdmin, admin.ModelAdmin):
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


@admin.register(Acquisition)
class AcquisitionAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_filter = ('method', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'title', 'method', 'date_start', 'date_end')
    search_fields = ['__all__']
    filter_horizontal = ('source', 'dealer', )
    form = AcquisitionAdminForm
