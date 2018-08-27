from django.contrib import admin
from django import forms
from django.conf import settings

# Project Guia imports
from .models import *
from person.models import Person
## Third part imports ##
from django.utils.translation import ugettext_lazy
from ckeditor.widgets import CKEditorWidget
from django_admin_json_editor import JSONEditorWidget
from reversion_compare.admin import CompareVersionAdmin
import tablib
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('uuid',)
        exclude = ('id_auto_series')


@admin.register(Post)
class PostAdmin(CompareVersionAdmin, ImportExportModelAdmin):
    readonly_fields = ('created', 'uuid', 'slug',)
    resource_class = PostResource
    filter_horizontal = ('capture',)
