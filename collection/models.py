from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

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
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('ex.: basic - 0'),
        verbose_name=_('title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('the description of level type...'),
        verbose_name=_('description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Description level')
        verbose_name_plural=_('Description levels')


class AggregationType(models.Model):
    """Used to label collections or Sets according type of Aggregation"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('ex.: collection, archive, etc'),
        verbose_name=_('title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('ex.: the collection is a group of...'),
        verbose_name=_('description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Aggregation Type')
        verbose_name_plural=_('Aggregations Type')


class GenreTag(models.Model):
    """Used to label collections, Sets or Items according content genre type"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('ex.: photo, picture, draw, etc'),
        verbose_name=_('title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text='Ex.: ',
        verbose_name='Descrição')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('genre tag')
        verbose_name_plural = _('genre tags')


class Thumbnail(models.Model):
    """Used to record thumbnail images of representative classes like collections, sets, items, Persons, Exhibitions, etc"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('auto set field'),
        verbose_name=_('universally unique identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('ex.: image title, like "the photographer resting" '),
        verbose_name=_('title'))
    image = models.ImageField(
        null=True,
        blank=True,
        help_text=_('ex.: image file'),
        verbose_name=_('image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('thumbnail')
        verbose_name_plural = _('thumbnails')


class Item(models.Model):
    """Used to store archive items like photos, pictures, etc"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('auto set field'),
        verbose_name=_('universally unique identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('institucional human identifier'),
        verbose_name=_('id'))
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('ex.: Salgado Negative - 001'),
        verbose_name=_('title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('ex.: gelatin negative of the first photo...'),
        verbose_name=_('title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')


class Sets(models.Model):
    """Used to store an aggroupment of items"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('auto set field'),
        verbose_name=_('universally unique identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('institucional container human identifier'),
        verbose_name=_('id'))
    aggregation_type = models.ForeignKey(
        AggregationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('container aggregation type'),
        verbose_name=_('aggregation type'))
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('ex.: container of...'),
        verbose_name=_('title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('ex.: this container is...'),
        verbose_name=_('description'))
    items = models.ManyToManyField(
        Item,
        blank=True,
        help_text=_('itens that composes the container'),
        verbose_name=_('items'))
    description_level = models.ForeignKey(
        DescriptionLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('choose a description level to this container'),
        verbose_name=_('description level'))
    sets_child = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('choose child containers to aggregate to this one'),
        verbose_name=_('child containers'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('container')
        verbose_name_plural = _('containers')


class AccessCondition(models.Model):
    """Used to store access condition concerned of items, sets os collections"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    title_short = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text=_('ex.: Full Free, Partial, Retricted'),
        verbose_name=_('access'))
    title_long = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text=_('ex.: Partial - copyright'),
        verbose_name=_('title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('ex.: Some documents here have copyright...'),
        verbose_name=_('description'))

    def __str__(self):
        return self.title_short

    class Meta:
        verbose_name = _('access condition')
        verbose_name_plural = _('access conditions')


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
        help_text=_('auto set field'),
        verbose_name=_('universally unique identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('auto set field'),
        verbose_name=_('created in'))
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('institucional collection human identifier'),
        verbose_name=_('id'))
    id_old = JSONField(
        null=True,
        blank=True,
        help_text=_('legacy identifiers'),
        verbose_name=_('old ids'))
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('the complete photo collection of Sebastião Salgado'),
        verbose_name=_('title'))
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('ex.: complete-collection-sebastiao-salgado'),
        verbose_name=_('slug'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('ex.: this collection is composed by...'),
        verbose_name=_('abstract'))
    fulltext = models.TextField(
        null=True,
        blank=True,
        help_text=_('ex.: All itens in this collection...'),
        verbose_name=_('full text'))
    description_level = models.ForeignKey(
        DescriptionLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('choose an option'),
        verbose_name=_('description level'))
    aggregation_type = models.ForeignKey(
        AggregationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('choose an option'),
        verbose_name=_('aggregation type'))
    genre_tags = models.ForeignKey(
        GenreTag,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('choose one or more options'),
        verbose_name=_('genre tags'))
    dimensions = JSONField(
        null=True,
        blank=True,
        help_text=_('feed with information about dimensions'),
        verbose_name=_('dimensions'))
    date_start = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_('choose a start date'),
        verbose_name=_('initial date'))
    date_start_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('choose a start date caption'),
        verbose_name=_('initial date caption'))
    date_end = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_('choose an final date'),
        verbose_name=_('final date'))
    date_end_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('choose a final date caption'),
        verbose_name=_('final date caption'))
    thumbnail = models.ManyToManyField(
        Thumbnail,
        blank=True,
        help_text=_('choose some introduction and representative images'),
        verbose_name=_('thumbnails'))
    author = models.ManyToManyField(
        Person,
        blank=True,
        help_text=_("choose some collection's authors"),
        verbose_name=_('authors'))
    sets = models.ManyToManyField(
        Sets,
        blank=True,
        help_text=_('choose containers that compose the collection'),
        verbose_name=_('containers'))
    items = models.ManyToManyField(
        Item,
        blank=True,
        help_text=_('choose some items that compose this collection. ATTENTION: You can create a container and aggregate items there'),
        verbose_name=_('items'))
    items_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('total collection items'),
        verbose_name=_('total items'))
    items_processed = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('total processed items'),
        verbose_name=_('processed items'))
    items_online = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('total online collection items'),
        verbose_name=_('online items'))
    access_condition = models.ForeignKey(
        AccessCondition,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('choose the more appropriate access condition to this collection'),
        verbose_name=_('access condition'))
    access_local_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('local access status'),
        verbose_name=_('is there any local access to the collection?'))
    access_online_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('is there any online access to the collection?'),
        verbose_name=_('online access status'))
    access_link = models.URLField(
        null=True,
        blank=True,
        help_text=_('do you have some online link access to this collection?'),
        verbose_name=_('access link'))
    location_generic = models.ManyToManyField(
        Location,
        blank=True,
        help_text=_('what is the generic location to the collection?'),
        verbose_name=_('generic location'))
    location_specific = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('what is the specific location to this collection?'),
        verbose_name=_('specific location'))
    inventary_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('is there any inventary to this collection?'),
        verbose_name=_('inventary status'))
    inventary_last_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('what is the inventary last date?'),
        verbose_name=_('inventary last date'))
    inventary_data = JSONField(
        null=True,
        blank=True,
        help_text=_('several data about the inventary'),
        verbose_name=_('inventary data'))
    management_unit = models.ManyToManyField(
        ManagementUnit,
        blank=True,
        help_text=_('what is the management unit concerning to this collection?'),
        verbose_name=_('management unit'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('other unstructured data of this collection'),
        verbose_name=_('other data'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'pk': self.uuid})

    def get_absolute_url_slug(self):
        return reverse('collection_detail_slug', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collections')
