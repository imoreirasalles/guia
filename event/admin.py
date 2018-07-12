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


@admin.register(EventType)
class EventTypeAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'created', 'title', 'description')
    search_fields = ['id', 'created', 'title', 'description']


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


@admin.register(Event)
class EventAdmin(VersionAdmin, admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('type', 'location', 'date_start', 'date_end')
    list_display = ('id', 'created', 'title', 'date_start', 'date_end', 'type', 'location')
    search_fields = ['id', 'created', 'title', 'date_start', 'date_end', 'type__title', 'location__title']
    form = EventAdminForm
