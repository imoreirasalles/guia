from django.contrib import admin
from django import forms
# Project Guia imports
from .models import *
## Third part imports ##
# Froala WYSWYG editor https://github.com/froala/django-froala-editor
from froala_editor.widgets import FroalaEditor


admin.site.register(Thumbnail)
admin.site.register(DescriptionLevel)
admin.site.register(AggregationType)
admin.site.register(GenreTag)
admin.site.register(Item)
admin.site.register(Sets)
admin.site.register(AccessCondition)


class CollectionAdminForm(forms.ModelForm):
    abstract = forms.CharField(widget=FroalaEditor)

    class Meta:
       model = Collection
       fields = '__all__'
       labels = {
        'abstract': ('Resumo')
       }
       help_texts = {
        'abstract': ('Resumo')
       }
       verbose_name = {
        'abstract': ('Resumo')
       }


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    form = CollectionAdminForm
