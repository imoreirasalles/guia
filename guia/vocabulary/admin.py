from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from .models import Term, Vocabulary


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('label', 'summary', 'id_human', 'semantic_url')
    fields = ('label', 'summary', 'id_human', 'semantic_url', 'extra')


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('label', 'summary', 'id_human', 'semantic_url')
    filter_horizontal = ('terms',)
    fields = ('label', 'summary', 'id_human', 'semantic_url', 'terms',)
