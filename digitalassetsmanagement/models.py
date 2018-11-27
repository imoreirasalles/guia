from guia.models import Base
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
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
        help_text=_('Choose the image whish represents this image'),
        verbose_name=_('Image'))

    def __str__(self):
        if self.image:
            Capture_file_str = '{} IMG [{}]'.format(self.title, str(self.image))
        else:
            self.image = _('No file image')
            Capture_file_str = 'IMG [{}]'.format(str(self.image))
        Capture_id_str = 'ID [' + str(self.id_auto_series) + '] '
        return (Capture_id_str + "  " + Capture_file_str)

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            super(Capture, self).save(*args, **kwargs)

        slug_auto = slugify(str(self.id_auto_series) + '-image-' + self.title)

        self.slug = slug_auto
        super(Capture, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


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
        help_text=_('Image(s) taked from this item.'),
        verbose_name=_('Image(s)'))

    def __str__(self):
        if self.title == None:
            item_str = str(self.uuid)
        else:
            item_str = (str(self.id_auto_series) + ': ' + self.title)
        return item_str

    def save(self, *args, **kwargs):
        if self.title == None:
            item_title_str = '[no title]'
        else:
            item_title_str = self.title
        if self.id_auto_series == None:
            super(Item, self).save(*args, **kwargs)
            item_id_str = str(self.id_auto_series)
        else:
            item_id_str = str(self.id_auto_series)
        if self.id_human == None:
            item_id_human_str = ' '
        else:
            item_id_human_str = str(self.id_human)

        slug_auto = slugify(item_id_str + '-item-' +
                            item_id_human_str + '-' +
                            item_title_str)
        self.slug = slug_auto
        super(Item, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
