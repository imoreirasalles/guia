from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import HStoreField
from django.contrib.postgres.fields import JSONField

# Third part imports
import uuid

# Project guia imports
from person.models import *

class DescriptionLevel(models.model):
    """Used to label collections according less or more description have an instance"""
    created = models.DateTimeField(editable=False, auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title


class AggregationType(models.model):
    """Used to label collections or Sets according type of Aggregation"""
    created = models.DateTimeField(editable=False, auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title


class GenreTags(models.model):
    """Used to label collections, Sets or Items according content genre type"""
    created = models.DateTimeField(editable=False, auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.title


class Thumbnail(models.Model):
    """Used to record thumbnail images of representative classes like collections, sets, items, Persons, Exhibitions, etc"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Sets(models.Model):
    """Used to store an aggroupment of items"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    aggregation_type = models.ForeignKey(AggregationType, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256, null=False, blank=True)
    abstract = models.TextField(null=True, blank=True)
    items = models.ManyToManyField(Item, null=True, blank=True, on_delete=models.SET_NULL)
    description_level = models.ForeignKey(DescriptionLevel, null=True, blank=True, on_delete=models.SET_NULL)
    sets_child = models.ForeignKey(Sets, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Item(models.Model):
    """Used to store archive items like photos, pictures, etc"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    title = models.CharField(max_length=256, null=False, blank=True)
    abstract = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class AccessCondition(models.Model):
    """Used to store access condition concerned of items, sets os collections"""
    title_short = models.CharField(max_length=64, null=False, blank=True)
    title_long = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_short


class Collection(models.Model):
    """
    Main class of collection
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    id = models.CharField(max_length=64, null=True, blank=True, unique=True)
    id_old = HStoreField(null=True, blank=True)
    title = models.CharField(max_length=256, null=False, blank=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    fulltext = models.TextField(null=True, blank=True)
    description_level = models.ForeignKey(DescriptionLevel, null=True, blank=True, on_delete=models.SET_NULL)
    aggregation_type = models.ForeignKey(AggregationType, null=True, blank=True, on_delete=models.SET_NULL)
    genre_tags = models.ForeignKey(GenreTags, null=True, blank=True, on_delete=models.SET_NULL)
    dimension = JSONField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_start_caption = models.CharField(max_length=64, null=False, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    date_end_caption = models.CharField(max_length=64, null=False, blank=True)
    thumbnail = models.ForeignKey(Thumbnail, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ManyToManyField(Person, null=True, blank=True, on_delete=models.SET_NULL)
    sets = models.ManyToManyField(Sets, null=True, blank=True, on_delete=models.SET_NULL)
    items = models.ManyToManyField(Item, null=True, blank=True, on_delete=models.SET_NULL)
    items_total =
    items_processed =
    items_online =
    access_condition =
    access_local_status =
    access_online_status =
    access_link =
    location_generic =
    location_specific =
    inventary_status =
    inventary_last_date =
    inventary_data =
    management_unit =
    other_data = JSONField(null=True, blank=True)

    def __str__(self):
        return self.title
