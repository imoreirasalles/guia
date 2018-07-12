from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Third part imports
import uuid
import reversion

# Project Apps Imports
from django.apps import apps


@reversion.register()
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


@reversion.register()
class Capture(models.Model):
    """Store captures of items"""
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
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: The capture title'),
        verbose_name=_('Title'))
    thumbnail = models.ForeignKey(
        Thumbnail,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the image whish represents this capture'),
        verbose_name=_('Thumbnails'))

    class Meta:
        verbose_name = _('Capture')
        verbose_name_plural = _('Captures')


@reversion.register()
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
        help_text=_('Ex.: Salgado Negative - 001'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: Gelatin negative of the first photo...'),
        verbose_name=_('Title'))
    capture = models.ManyToManyField(
        Capture,
        blank=True,
        help_text=_('Capture(s) taked from this item.'),
        verbose_name=_('Capture(s)'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
