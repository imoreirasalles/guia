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


@admin.register(PublicationType)
class PublicationTypeAdmin(CompareVersionAdmin, admin.ModelAdmin):
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


@admin.register(Publication)
class PublicationAdmin(CompareVersionAdmin, admin.ModelAdmin):
    list_display = ('id_auto_series', 'uuid', 'title', 'date_released')
    search_fields = ['__all__']
    filter_horizontal = ('author', 'publisher')
    form = PublicationAdminForm
