from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


class ExhibitionAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))

    class Meta:
        model = Exhibition
        fields = '__all__'


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_filter = ('location', 'date_start', 'date_end')
    list_display = ('title', 'location', 'date_start', 'date_end', 'link')
    search_fields = ['uuid', 'title', 'date_start', 'date_end', 'team']
    filter_horizontal = ('catalog', 'publication')
    form = ExhibitionAdminForm


@admin.register(ExhibitionEdition)
class ExhibitionEditionAdmin(admin.ModelAdmin):
    list_filter = ('location', 'date_start', 'date_end')
    list_display = ('title', 'location', 'date_start', 'date_end')
    search_fields = ['uuid', 'title', 'date_start', 'date_end', 'team']
