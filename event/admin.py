from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'created', 'title', 'description')
    search_fields = ['id', 'created', 'title', 'description']


class EventAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('type', 'location', 'date_start', 'date_end')
    list_display = ('id', 'created', 'title', 'date_start', 'date_end', 'type', 'location')
    search_fields = ['id', 'created', 'title', 'date_start', 'date_end', 'type__title', 'location__title']
    form = EventAdminForm
