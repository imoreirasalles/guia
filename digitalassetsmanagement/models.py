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
class Capture(Base):
    """Used to record capture images of items. Faced in representative classes like collections, containers, items, Persons, Exhibitions, etc"""
    image = models.ImageField(
        null=True,
        blank=True,
        help_text=_('Choose the image whish represents this capture'),
        verbose_name=_('Capture'))

    def __str__(self):
        if self.image != None:
            Capture_file_str = 'IMG [' + str(self.image) + ']'
        else:
            self.image = _('No file image')
            Capture_file_str = 'IMG [' + str(self.image) + ']'
        Capture_id_str = 'ID [' + str(self.id_auto_series) + '] '
        return (Capture_id_str + "  " + Capture_file_str)

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
