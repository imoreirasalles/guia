from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from guia.models import Base
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# Third part imports
import reversion
from reversion.models import *
# Project Apps Imports
from django.apps import apps


@reversion.register()
class Post(Base):
    """Used to store the home welcome content"""
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: Welcome to Guia...'),
        verbose_name=_('Content'))
    capture = models.ManyToManyField(
        'digitalassetsmanagement.capture',
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Images'))

    def __str__(self):
        if self.title == None:
            Container_str = str(self.uuid)
        else:
            Container_str = self.title
        return Container_str

    class Meta:
        verbose_name = _('Home Post')
        verbose_name_plural = _('Home Posts')
