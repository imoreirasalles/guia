# Core django imports
from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
from django.conf import settings
from django.utils.translation import gettext_lazy as _
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget


PERSON_TYPES = (
    ('individual', _('Individual')),
    ('juridical', _('Juridical'))
)

GENDER = (
    ('m', 'Male'),
    ('f', 'Female')
)


class PersonAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Text'))
    person_type = forms.ChoiceField(
        required=False,
        choices=PERSON_TYPES,
    )
    gender = forms.ChoiceField(
        required=False,
        choices=GENDER,
    )
    linked_open_data = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Linked Open Data Dictionary'))


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_filter = ('person_type', 'is_staff', 'is_partner', 'is_feature', 'gender', 'date_start', 'date_end')
    list_display = ('uuid', 'id', 'person_type', 'title', 'gender')
    search_fields = ('uuid', 'title')
    filter_horizontal = ('thumbnail',)
    form = PersonAdminForm
