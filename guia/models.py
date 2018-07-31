from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from django.utils.translation import pgettext_lazy
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db import IntegrityError
from django.shortcuts import render_to_response
from datetime import datetime
# Third part imports
import uuid

# Project Apps Imports
from django.apps import apps


class Base(models.Model):
    """Used to base models with uuid, """
    id_auto_series = models.BigAutoField(
        primary_key=True,
        editable=False,
        help_text=_('Auto Increment ID'),
        verbose_name=_('ID'))
    created = models.DateTimeField(
        default=datetime.now,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    uuid = models.UUIDField(
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Universal Unique Identifier'))
    title = models.CharField(
        default=None,
        max_length=256,
        help_text=_('Ex.: The title of this record'),
        verbose_name=_('Title'))
    slug = models.SlugField(
        default=None,
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Ex.: complete-collection-sebastiao-salgado'),
        verbose_name=_('Slug'))

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            super(Base, self).save(*args, **kwargs)

        slug_auto = slugify( str(self.id_auto_series) + '_' + self.title)
        self.slug = slug_auto
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True
