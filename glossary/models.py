from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from guia.models import Base
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Third part imports
import reversion

# Project Apps Imports
from django.apps import apps


@reversion.register()
class DescriptionLevel(Base):
    """Used to label collections according less or more description have an instance"""
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


@reversion.register()
class AggregationType(Base):
    """Used to label collections or containers according type of Aggregation"""
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


@reversion.register()
class GenreTag(Base):
    """Used to label collections, containers or Items according content genre type"""
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


@reversion.register()
class AccessCondition(Base):
    """Used to store access condition concerned of captures, items, containers and collections"""
    title_long = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text=_('Ex.: Partial - copyright.'),
        verbose_name=_('Condition'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: Some documents here have copyright...'),
        verbose_name=_('Description'))

    def __str__(self):
        if self.title_long != None:
            AccessCondition_str = str(self.title) + str(': ') + str(self.title_long)
        else:
            AccessCondition_str = self.title + ':' + _('No condition')
        return AccessCondition_str

    class Meta:
        verbose_name = _('Access Condition')
        verbose_name_plural = _('Access Conditions')
