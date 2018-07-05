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
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: basic - 0'),
        verbose_name=_('Title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('The description of level type...'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Description level')
        verbose_name_plural=_('Description levels')


class AggregationType(models.Model):
    """Used to label collections or containers according type of Aggregation"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: collection, archive, etc'),
        verbose_name=_('Title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('Ex.: the collection is a group of...'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Aggregation Type')
        verbose_name_plural=_('Aggregations Type')


class GenreTag(models.Model):
    """Used to label collections, containers or Items according content genre type"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: photo, picture, draw, etc'),
        verbose_name=_('Title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('Ex.: A photo is all kind part or entire piece of an image produced by a camera.'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Genre Tag')
        verbose_name_plural = _('Genre Tags')


class Thumbnail(models.Model):
    """Used to record thumbnail images of representative classes like collections, containers, items, Persons, Exhibitions, etc"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Universal Unique Identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: Image title, like "the photographer resting" '),
        verbose_name=_('Title'))
    image = models.ImageField(
        null=True,
        blank=True,
        help_text=_('The Image File'),
        verbose_name=_('Image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Thumbnail')
        verbose_name_plural = _('Thumbnails')


class Item(models.Model):
    """Used to store archive items like photos, pictures, etc"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Universal Unique Identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Created in'))
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Human Identifier'),
        verbose_name=_('ID'))
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('ex.: Salgado Negative - 001'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: Gelatin negative of the first photo...'),
        verbose_name=_('Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')


class Container(models.Model):
    """Used to store an aggroupment of items"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Universal Unique Identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Created in'))
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Container Human Identifier'),
        verbose_name=_('ID'))
    aggregation_type = models.ForeignKey(
        AggregationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Container Aggregation Type'),
        verbose_name=_('Aggregation Type'))
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('Ex.: Container of...'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This container is...'),
        verbose_name=_('Description'))
    items = models.ManyToManyField(
        Item,
        blank=True,
        help_text=_('Itens that composes the container'),
        verbose_name=_('Items'))
    description_level = models.ForeignKey(
        DescriptionLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose a description level to this container'),
        verbose_name=_('Description level'))
    container_child = models.ManyToManyField(
        'self',
        blank=True,
        help_text=_('Choose child containers to aggregate to this one'),
        verbose_name=_('Child containers'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Container')
        verbose_name_plural = _('Containers')


class AccessCondition(models.Model):
    """Used to store access condition concerned of captures, items, containers and collections"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title_short = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text=_('Ex.: Full Free, Partial, Retricted, etc.'),
        verbose_name=_('Access'))
    title_long = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text=_('Ex.: Partial - copyright.'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: Some documents here have copyright...'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title_short

    class Meta:
        verbose_name = _('Access Condition')
        verbose_name_plural = _('Access Conditions')


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
        help_text=_('This is an auto set field'),
        verbose_name=_('Universal Unique Identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Created in'))
    id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Collection Human Identifier'),
        verbose_name=_('ID'))
    id_old = JSONField(
        null=True,
        blank=True,
        help_text=_('Legacy Identifiers'),
        verbose_name=_('Old IDs'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: The complete photo collection of Sebastião Salgado.'),
        verbose_name=_('Title'))
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Ex.: complete-collection-sebastiao-salgado'),
        verbose_name=_('Slug'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This collection is composed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: All itens in this collection...'),
        verbose_name=_('Full Text'))
    description_level = models.ForeignKey(
        DescriptionLevel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose an Option'),
        verbose_name=_('Description Level'))
    aggregation_type = models.ForeignKey(
        AggregationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose an Option'),
        verbose_name=_('Aggregation Type'))
    genre_tags = models.ForeignKey(
        GenreTag,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose one or more options'),
        verbose_name=_('Genre Tags'))
    dimensions = JSONField(
        null=True,
        blank=True,
        help_text=_('Feed with information about dimensions'),
        verbose_name=_('Dimensions'))
    date_start = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    date_start_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Choose a start date caption'),
        verbose_name=_('Initial date caption'))
    date_end = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date'),
        verbose_name=_('Final date'))
    date_end_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Choose a final date caption'),
        verbose_name=_('Final date caption'))
    thumbnail = models.ManyToManyField(
        Thumbnail,
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Thumbnails'))
    author = models.ManyToManyField(
        Person,
        blank=True,
        help_text=_("Choose some collection's authors"),
        verbose_name=_('Authors'))
    container = models.ForeignKey(
        Container,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose containers that compose the collection'),
        verbose_name=_('Containers'))
    items = models.ManyToManyField(
        Item,
        blank=True,
        help_text=_('Choose some items that compose this collection. ATTENTION: You can create a container and aggregate items there'),
        verbose_name=_('Items'))
    items_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total collection items'),
        verbose_name=_('Total Items'))
    items_processed = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total processed items'),
        verbose_name=_('Processed Items'))
    items_online = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total online collection items'),
        verbose_name=_('Online Items'))
    access_condition = models.ForeignKey(
        AccessCondition,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the more appropriate access condition to this collection'),
        verbose_name=_('Access Condition'))
    access_local_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('Is there any local access to the collection?'),
        verbose_name=_('Local Access Status'))
    access_online_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('Is there any online access to the collection?'),
        verbose_name=_('Online Access Status'))
    access_link = models.URLField(
        null=True,
        blank=True,
        help_text=_('Do you have some online link access to this collection?'),
        verbose_name=_('Access Link'))
    location_generic = models.ManyToManyField(
        Location,
        blank=True,
        help_text=_('What is the generic location to the collection?'),
        verbose_name=_('Generic Location'))
    location_specific = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('What is the specific location to this collection?'),
        verbose_name=_('Specific Location'))
    inventary_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('Is there any inventary to this collection?'),
        verbose_name=_('Inventary Status'))
    inventary_last_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('What is the inventary last date?'),
        verbose_name=_('Inventary Last Date'))
    inventary_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Several data about the inventary'),
        verbose_name=_('Inventary Data'))
    management_unit = models.ManyToManyField(
        ManagementUnit,
        blank=True,
        help_text=_('What is the management unit concerning to this collection?'),
        verbose_name=_('Management Unit'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this collection'),
        verbose_name=_('Other Data'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'pk': self.uuid})

    def get_absolute_url_slug(self):
        return reverse('collection_detail_slug', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')
