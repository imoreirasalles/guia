from django.contrib import admin
from .models import *
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin


@admin.register(ManagementUnit)
class ManagementUnitAdmin(CompareVersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description')


@admin.register(AcquisitionMethod)
class AcquisitionMethodAdmin(CompareVersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description')


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
    readonly_fields = ['created']
    list_filter = ('method', 'date_start', 'date_end')
    list_display = ('uuid', 'title', 'method', 'date_start', 'date_end')
    search_fields = ('uuid', 'title')
    filter_horizontal = ('source', 'dealer', )
    form = AcquisitionAdminForm
