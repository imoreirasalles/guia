from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
from django.conf import settings
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget


@admin.register(PublicationType)
class PublicationTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description')


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
class PublicationAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'date_released')
    filter_horizontal = ('author', 'publisher')
    form = PublicationAdminForm
