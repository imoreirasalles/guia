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


PERSON_TYPES = (
    ('individual', _('Individual')),
    ('juridical', _('Juridical'))
)

GENDER = (
    ('m', _('Male')),
    ('f', _('Female'))
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


class PersonResource(resources.ModelResource):

    class Meta:
        model = Person
        fields = ('uuid', 'title', 'id_human', 'person_type', 'title_index', 'is_staff', 'is_partner', 'is_feature', 'gender', 'abstract', 'full_text', 'date_start', 'date_end', 'url', 'linked_open_data')
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Person)
class PersonAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = PersonResource
    list_filter = ('person_type', 'is_staff', 'is_partner', 'is_feature', 'gender', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'person_type', 'title', 'gender', 'is_draft')
    search_fields = ['__all__']
    filter_horizontal = ('capture',)
    form = PersonAdminForm
