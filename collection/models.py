from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models

# Third part imports
import uuid

# Project guia imports
from person.models import *
from management.models import *
from location.models import *


class DescriptionLevel(models.Model):
    """Used to label collections according less or more description have an instance"""
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação')
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Nível de Descrição'
        verbose_name_plural = 'Niveis de Descrição'


class AggregationType(models.Model):
    """Used to label collections or Sets according type of Aggregation"""
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do registro')
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tipo de Agregação'
        verbose_name_plural = 'Tipos de Agregação'


class GenreTag(models.Model):
    """Used to label collections, Sets or Items according content genre type"""
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do registro')
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tipologia de Gênero"
        verbose_name_plural = 'Tipologias de Gênero'


class Thumbnail(models.Model):
    """Used to record thumbnail images of representative classes like collections, sets, items, Persons, Exhibitions, etc"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        verbose_name='Identificador Único Universal')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do registro')
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    image = models.ImageField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Imagem')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Imagem de Apresentação"
        verbose_name_plural = "Imagens de apresentação"


class Item(models.Model):
    """Used to store archive items like photos, pictures, etc"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        verbose_name='Identificador Único Universal')
    created = models.DateTimeField(
        auto_now_add=True,
        help_text='Ex.: ',
        verbose_name='Data do Registro')
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text='Ex.: ',
        verbose_name='Identificador Institucional do Item')
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = "Itens"


class Sets(models.Model):
    """Used to store an aggroupment of items"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        verbose_name='Identificador Único Universal do Conjunto')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Registro')
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text='Ex.: ',
        verbose_name='Identificador Institucional')
    aggregation_type = models.ForeignKey(
        AggregationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Tipo de Agregação')
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Resumo')
    items = models.ManyToManyField(
        Item,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Items')
    description_level = models.ForeignKey(
        DescriptionLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Nível de Descrição')
    sets_child = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Conjuntos Filhos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Conjunto'
        verbose_name_plural = "Conjuntos"


class AccessCondition(models.Model):
    """Used to store access condition concerned of items, sets os collections"""
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do Registro')
    title_short = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título curto')
    title_long = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título Longo')
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição')

    def __str__(self):
        return self.title_short

    class Meta:
        verbose_name = 'Condição de Acesso'
        verbose_name_plural = "Condições de Acesso"


class Collection(models.Model):
    """
    Main class of collection
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        verbose_name='Identificador Universal do Registro')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do Registro')
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text='Ex.: ',
        verbose_name='Identificador Institucional')
    id_old = JSONField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Identificadores Legados')
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Título')
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Apelido único(slug)')
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Resumo')
    fulltext = models.TextField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição Completa')
    description_level = models.ForeignKey(
        DescriptionLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Nível de descrição')
    aggregation_type = models.ForeignKey(
        AggregationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Tipo de Agregação')
    genre_tags = models.ForeignKey(
        GenreTag,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Gêneros da Coleção')
    dimension = JSONField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Dimensões')
    date_start = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Data de Inicio')
    date_start_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Legenda da Data de Inicio')
    date_end = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Data Final')
    date_end_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Legenda da Data Final')
    thumbnail = models.ManyToManyField(
        Thumbnail,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Imagens de apresentação')
    author = models.ManyToManyField(
        Person,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Pessoas Relacionadas')
    sets = models.ManyToManyField(
        Sets,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Conjuntos Relacionados')
    items = models.ManyToManyField(
        Item,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Itens Relacionados')
    items_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Total de itens')
    items_processed = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Itens Processados')
    items_online = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Itens online')
    access_condition = models.ForeignKey(
        AccessCondition,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Ex.: ',
        verbose_name='Condição de Acesso')
    access_local_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Possui acesso local?')
    access_online_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Possui acesso online?')
    access_link = models.URLField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Link de Acesso Digital')
    location_generic = models.ManyToManyField(
        Location,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Localização Genérica')
    location_specific = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Localização Específica')
    inventary_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Possui inventário?')
    inventary_last_date = models.DateField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Data do último inventário')
    inventary_data = JSONField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Dados do Inventário')
    management_unit = models.ManyToManyField(
        ManagementUnit,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Área de Governança ou Coordenação')
    other_data = JSONField(
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Outros Dados Não-Estruturados')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Coleção'
        verbose_name_plural = "Coleções"
