from django.db import models
from django.contrib import admin
from reversion.admin import VersionAdmin
from jsonfield import JSONField


@admin.register(Collection)
class Collection(VersionAdmin):
    uuid
    id_old   | JSON    | Dicionário de todos os códigos já utilizados para identificar a Coleção | {"Instituição 1": "ABC", "Instituição 2": "123"}
    title    | CharField  | Título completo da Coleção | Biblioteca de Fulano de Tal
    slug     | String  | Título curto da Coleção | Biblioteca Fulado
    abstract | String  | Breve apresentação da Coleção | 02/08/2018
    unstructured_data | JSON    | Dicionário com quantificação preliminar dos objetos identificados | {"Fotografias": "1439", "Cadernos": "12"}
