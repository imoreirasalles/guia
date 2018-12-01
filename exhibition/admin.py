from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin
import tablib
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from digitalassetsmanagement.models import Capture
from digitalassetsmanagement.widgets import MultipleSelectPreviewImageWidget



class ExhibitionResource(resources.ModelResource):
    # id_human = Field(attribute='id_human', column_name='Identificador Institucional')
    # title = Field(attribute='title', column_name='Título')
    # abstract = Field(attribute='abstract', column_name='Resumo da Exposição')
    # full_text = Field(attribute='full_text', column_name='Apresentação Completa da Exposição')
    # date_start = Field(attribute='date_start', column_name='Data de Lançamento da Exposição - AAAA-MM-DD')
    # date_end = Field(attribute='date_end', column_name='Data de Encerramento da Exposição - AAAA-MM-DD')
    # link = Field(attribute='link', column_name='Link - EX.: http://ims.com.br')
    class Meta:
        model = Exhibition
        fields = ('uuid', 'title', 'id_human', 'abstract', 'full_text', 'date_start', 'date_end', 'link')
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


class ExhibitionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))
    team = forms.CharField(
        required=False,
        widget=JSONEditorWidget(settings.DATA_SCHEMA, collapsed=False),
        label=_('Team'))
    capture = forms.ModelMultipleChoiceField(
        queryset=Capture.objects.all(),
        label=_('Image'),
        required=False,
        widget=MultipleSelectPreviewImageWidget()
    )

    class Meta:
        model = Exhibition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['capture'].widget = RelatedFieldWidgetWrapper(
            self.fields['capture'].widget,
            Exhibition._meta.get_field('capture').remote_field,
            self.admin_site
        )


@admin.register(Exhibition)
class ExhibitionAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = ExhibitionResource
    list_filter = ('date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'title', 'date_start', 'date_end', 'link', 'is_draft')
    search_fields = ['id_auto_series', 'uuid', 'title', 'date_start', 'date_end', 'team']
    filter_horizontal = ('catalog', 'publication', 'capture')
    form = ExhibitionAdminForm

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.form.admin_site = admin_site


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


class ExhibitionEditionResource(resources.ModelResource):

    class Meta:
        model = ExhibitionEdition


@admin.register(ExhibitionEdition)
class ExhibitionEditionAdmin(CompareVersionAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = ExhibitionEditionResource
    list_filter = ('location', 'date_start', 'date_end')
    list_display = ('id_auto_series', 'uuid', 'title', 'location', 'date_start', 'date_end')
    search_fields = ['id_auto_series', 'uuid', 'title', 'date_start', 'date_end', 'team']
    form = ExhibitionEditionAdminForm
