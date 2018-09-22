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


class EventTypeResource(resources.ModelResource):

    class Meta:
        model = EventType
        fields = ('uuid', 'title', 'description')
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(EventType)
class EventTypeAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = EventTypeResource
    list_display = ('id_auto_series', 'title', 'description')
    search_fields = ['__all__']


class EventAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))
    team = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Team'))
    other_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Other Unstructured Data')
    )

    class Meta:
        model = Event
        fields = '__all__'


class EventResource(resources.ModelResource):

    class Meta:
        model = Event
        fields = ('uuid', 'title', 'id_human', 'date_start', 'date_end', 'type', 'location', 'abstract', 'full_text',)
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Event)
class EventAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = EventResource
    list_filter = ('type', 'location', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'title', 'date_start', 'date_end', 'type', 'location')
    search_fields = ['__all__']
    form = EventAdminForm
