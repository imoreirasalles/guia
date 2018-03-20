from django.contrib import admin
from .models import Colecao, Pessoa, Lote, Exhibition, Publication

class ColecaoInline(admin.TabularInline):
	model = Colecao.pessoas.through

class LoteInline(admin.TabularInline):
	model = Lote

class PessoaAdmin(admin.ModelAdmin):
	list_display = ('name', 'ocupacao', 'date_of_birth', 'date_of_death',)
	list_display_links = ('name',)
	search_fields = ('name',)
	inlines = [
		ColecaoInline,
	]

class ColecaoAdmin(admin.ModelAdmin):
	fieldsets = [
		('Identificação Básica', {'fields': [('id', 'old_id'), 'title', 'area_ims']}),
		('Entrada na instituição', {'fields': [('entry_model', 'entry_date'), 'entry_obs']}),
		('Apresentação da coleção', {'fields': [('num_itens', 'num_itens_online'), 'resumo']}),
		('Entidades relacionadas', {'fields': ['pessoas']}),
		('Teste de JSON', {'fields': ['teste_json']}),
		('Teste de Array', {'fields': ['teste_array']})
	]
	list_display = ('id', 'old_id', 'area_ims', 'title', 'entry_model', 'entry_date', 'num_itens')
	list_display_links = ('id', 'title')
	list_filter = ('area_ims', 'entry_model')
	search_fields = ('id', 'old_id', 'title',)

class LoteAdmin(admin.ModelAdmin):
	list_display = ('entry_date', 'entry_model', 'colecao', 'entry_obs',)
	search_fields = ('entry_obs',)

class ExhibitionAdmin(admin.ModelAdmin):
	list_display = ('title', 'location', 'date_of_begin', 'date_of_end', 'description',)
	list_display_links = ('title',)
	search_fields = ('title', 'description')
	list_filter = ('location',)


admin.site.register(Colecao, ColecaoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Lote, LoteAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Publication)

admin.AdminSite.site_header = 'Instituto Moreira Salles'
admin.AdminSite.site_title = 'IMS'
admin.AdminSite.index_title = 'Painel de Controle'
