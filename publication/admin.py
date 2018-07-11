from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
# Project Guia imports
from .models import *
## Third part imports ##
from ckeditor.widgets import CKEditorWidget


@admin.register(PublicationType)
class PublicationTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'description')


class PublicationAdminForm(forms.ModelForm):
    full_text = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
        label=_('Full Description'))

    class Meta:
        model = Publication
        fields = '__all__'


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('id', 'title', 'date_released')
    filter_horizontal = ('author', 'publisher')
    form = PublicationAdminForm
