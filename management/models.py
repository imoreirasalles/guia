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
class ManagementUnit(Base):
    """Used to store unit of institutional management"""
    title = models.CharField(
        max_length=256,
        help_text=_('Title of Management Unit'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('The description of Management Unit'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Management Unit')
        verbose_name_plural = _('Management Units')


@reversion.register()
class Procedure(Base):
    """Used to store unit of institutional management"""
    title = models.CharField(
        max_length=256,
        help_text=_('Title of Procedure'),
        verbose_name=_('Title'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: this acquisition is composed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: All itens in this acquisition...'),
        verbose_name=_('Full Text'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this collection'),
        verbose_name=_('Other Data'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Procedure')
        verbose_name_plural = _('Procedures')


@reversion.register()
class AcquisitionMethod(Base):
    """docstring for AquisitionMethod"""
    title = models.CharField(
        max_length=128,
        help_text=_('Type of acquisition method'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('The description of acquisition method'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Acquisition Method')
        verbose_name_plural = _('Acquisition Methods')


@reversion.register()
class Acquisition(Base):
    """Used to store diferent acquisitions"""
    title = models.CharField(
        max_length=256,
        help_text=_('Ex.: Aquisition from The Photographer...'),
        verbose_name=_('Title'))
    method = models.ForeignKey(
        AcquisitionMethod,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose an Option'),
        verbose_name=_('Aquisition Method'))
    source = models.ManyToManyField(
        'person.Person',
        related_name='personSource',
        blank=True,
        help_text=_('Choose people who have been source to this acquisition'),
        verbose_name=_('Source'))
    dealer = models.ManyToManyField(
        'person.Person',
        related_name='personDealer',
        blank=True,
        help_text=_('Choose people who traded this asset'),
        verbose_name=_('Dealer'))
    date_start = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    date_end = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date - special for lending'),
        verbose_name=_('Final Date'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: this acquisition is composed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: All itens in this acquisition...'),
        verbose_name=_('Full Text'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this collection'),
        verbose_name=_('Other Data'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Acquisition')
        verbose_name_plural = _('Acquisitions')
