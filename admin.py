from django.contrib import admin
from .models import Colecao, Pessoa

class ColecaoInline(admin.TabularInline):
	model = Colecao.pessoas.through 

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
		('Entidades relacionadas', {'fields': ['pessoas']})
	]
	list_display = ('id', 'old_id', 'area_ims', 'title', 'entry_model', 'entry_date', 'num_itens')
	list_display_links = ('id', 'title')
	list_filter = ('area_ims', 'entry_model') 
	search_fields = ('id', 'old_id', 'title',)

admin.site.register(Colecao, ColecaoAdmin)
admin.site.register(Pessoa, PessoaAdmin)

admin.AdminSite.site_header = 'Instituto Moreira Salles'
admin.AdminSite.site_title = 'IMS'
admin.AdminSite.index_title = 'Painel de Controle'
