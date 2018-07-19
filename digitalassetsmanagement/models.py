from guia.models import Base
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
class Thumbnail(Base):
    """Used to record thumbnail images of representative classes like collections, containers, items, Persons, Exhibitions, etc"""
    image = models.ImageField(
        help_text=_('The Image File'),
        verbose_name=_('Image'))

    def __str__(self):
        id_str = 'ID [' + str(self.id_auto_series) + '] '
        image_file_str = 'IMG [' + str(self.image) + ']'
        return (id_str + "  " + image_file_str)

    class Meta:
        verbose_name = _('Thumbnail')
        verbose_name_plural = _('Thumbnails')


@reversion.register()
class Capture(Base):
    """Store captures of items"""
    thumbnail = models.ForeignKey(
        Thumbnail,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the image whish represents this capture'),
        verbose_name=_('Thumbnails'))

    def __str__(self):
        id_str = 'ID [' + str(self.id_auto_series) + '] '
        image_file_str = 'IMG [' + str(self.thumbnail) + ']'
        return (id_str + "  " + image_file_str)

    class Meta:
        verbose_name = _('Capture')
        verbose_name_plural = _('Captures')


@reversion.register()
class Item(Base):
    """Used to store archive items like photos, pictures, etc"""
    id_human = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: Gelatin negative of the first photo...'),
        verbose_name=_('Description'))
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
