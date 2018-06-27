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
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Niveis de Descrição"


class AggregationType(models.Model):
    """Used to label collections or Sets according type of Aggregation"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tipos de Agregação"


class GenreTag(models.Model):
    """Used to label collections, Sets or Items according content genre type"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tipologias de Gênero"


class Thumbnail(models.Model):
    """Used to record thumbnail images of representative classes like collections, sets, items, Persons, Exhibitions, etc"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Imagens de apresentação"


class Item(models.Model):
    """Used to store archive items like photos, pictures, etc"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    title = models.CharField(max_length=256, null=False, blank=True)
    abstract = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Itens"


class Sets(models.Model):
    """Used to store an aggroupment of items"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    aggregation_type = models.ForeignKey(AggregationType, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256, null=False, blank=True)
    abstract = models.TextField(null=True, blank=True)
    items = models.ManyToManyField(Item, blank=True)
    description_level = models.ForeignKey(DescriptionLevel, null=True, blank=True, on_delete=models.SET_NULL)
    sets_child = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Conjuntos"


class AccessCondition(models.Model):
    """Used to store access condition concerned of items, sets os collections"""
    created = models.DateTimeField(auto_now_add=True)
    title_short = models.CharField(max_length=64, null=False, blank=True)
    title_long = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_short

    class Meta:
        verbose_name_plural = "Condições de Acesso"


class Collection(models.Model):
    """
    Main class of collection
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=64, null=True, blank=True, unique=True, help_text="Identificador único atribuido pelo IMS")
    id_old = JSONField(null=True, blank=True, help_text="Dicionário de códigos já utilizados para identificar a Coleção")
    title = models.CharField(max_length=256, null=False, blank=True, help_text="Título da Coleção")
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True, help_text="Nome amigável para a URL")
    abstract = models.TextField(null=True, blank=True, help_text="Breve apresentação da Coleção")
    fulltext = models.TextField(null=True, blank=True, help_text="Texto completo sobre a Coleção")
    description_level = models.ForeignKey(DescriptionLevel, null=True, blank=True, on_delete=models.SET_NULL)
    aggregation_type = models.ForeignKey(AggregationType, null=True, blank=True, on_delete=models.SET_NULL)
    genre_tags = models.ForeignKey(GenreTag, null=True, blank=True, on_delete=models.SET_NULL)
    dimension = JSONField(null=True, blank=True, help_text="Quantificação preliminar da dimensão")
    date_start = models.DateTimeField(null=True, blank=True, help_text="Data inicial do conteúdo da Coleção")
    date_start_caption = models.CharField(max_length=64, null=False, blank=True)
    date_end = models.DateTimeField(null=True, blank=True, help_text="Data final do conteúdo da Coleção")
    date_end_caption = models.CharField(max_length=64, null=False, blank=True)
    thumbnail = models.ManyToManyField(Thumbnail, blank=True)
    author = models.ManyToManyField(Person, blank=True, help_text="Autoridades sobre a coleção")
    sets = models.ManyToManyField(Sets, blank=True, help_text="Lista de conjuntos que integram a coleção")
    items = models.ManyToManyField(Item, blank=True, help_text="Lista de itens que integram a coleção")
    items_total = models.PositiveIntegerField(null=True, blank=True, help_text="Número total de itens na Coleção")
    items_processed = models.PositiveIntegerField(null=True, blank=True, help_text="Número total de itens processados")
    items_online = models.PositiveIntegerField(null=True, blank=True, help_text="Número total de itens disponíveis online")
    access_condition = models.ForeignKey(AccessCondition, null=True, blank=True, on_delete=models.SET_NULL)
    access_local_status = models.NullBooleanField(null=True, blank=True)
    access_online_status = models.NullBooleanField(null=True, blank=True)
    access_link = models.URLField(null=True, blank=True)
    location_generic = models.ManyToManyField(Location, blank=True)
    location_specific = models.CharField(max_length=256, null=False, blank=True)
    inventary_status = models.NullBooleanField(null=True, blank=True)
    inventary_last_date = models.DateField(null=True, blank=True)
    inventary_data = JSONField(null=True, blank=True, help_text="Quantificação preliminar do inventário")
    management_unit = models.ManyToManyField(ManagementUnit, blank=True, help_text="Qual coordenação é responsável pela Coleção")
    other_data = JSONField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Coleções"
