from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion.admin import VersionAdmin


class ExhibitionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))
    team = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Team'))

    class Meta:
        model = Exhibition
        fields = '__all__'


@admin.register(Exhibition)
class ExhibitionAdmin(VersionAdmin, admin.ModelAdmin):
    list_filter = ('location', 'date_start', 'date_end')
    list_display = ('title', 'location', 'date_start', 'date_end', 'link')
    search_fields = ['uuid', 'title', 'date_start', 'date_end', 'team']
    filter_horizontal = ('catalog', 'publication')
    form = ExhibitionAdminForm


class ExhibitionEditionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Text'))
    team = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Team'))

    class Meta:
        model = ExhibitionEdition
        fields = '__all__'


@admin.register(ExhibitionEdition)
class ExhibitionEditionAdmin(VersionAdmin, admin.ModelAdmin):
    list_filter = ('location', 'date_start', 'date_end')
    list_display = ('title', 'location', 'date_start', 'date_end')
    search_fields = ['uuid', 'title', 'date_start', 'date_end', 'team']
    form = ExhibitionEditionAdminForm
