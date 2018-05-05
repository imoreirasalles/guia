from django.contrib import admin
from guia.models import Colecao


@admin.register(Colecao)
class Colecao(admin.ModelAdmin):
    pass
