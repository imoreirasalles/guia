from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from .models import Term, Vocabulary


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("label", "summary", "semantic_url",)
    readonly_fields = ["created_at", "updated_at", "uuid", "slug",]

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('label', 'summary', 'id_human')
    filter_horizontal = ('terms',)
    fields = ('label', 'summary', 'terms', 'id_human')
