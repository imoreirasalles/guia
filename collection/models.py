from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import HStoreField
from django.contrib.postgres.fields import JSONField

# Third part imports
import uuid

# Project guia imports
from person.models import *


class Thumbnail(models.Model):
    """
    Thumbnail class used to record thumbnails of representative object images
    """
    uuid = models.UUIDField(default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Collection(models.Model):
    """
    Main class of collection
    """
    uuid = models.UUIDField(default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    id_ims = models.CharField(max_length=64, null=True, blank=True)
    id_old = HStoreField(null=True, blank=True)
    title = models.CharField(max_length=256, null=False)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    thumbnail = models.ForeignKey(Thumbnail, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ManyToManyField(Person)
    other_data = JSONField(null=True, blank=True)

    def __str__(self):
        return self.title
