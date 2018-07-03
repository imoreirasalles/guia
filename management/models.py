from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _

# Third part imports
import uuid

# Project guia imports
from person.models import *

class ManagementUnit(models.Model):
    """Used to store unit of institutional management"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field.'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        help_text=_('Title of Management Unit.'),
        verbose_name=_('Title'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('The description of Management Unit.'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Management Unit')
        verbose_name_plural = _('Management Units')


class AcquisitionMethod(models.Model):
    """docstring for AquisitionMethod"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Acquisition Method')
        verbose_name_plural = _('Acquisition Methods')


class Acquisition(models.Model):
    """Used to store diferent acquisitions"""
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('Auto set field'),
        verbose_name=_('Universal Unique Identifier'))
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
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
        Person,
        related_name='personSource',
        blank=True,
        help_text=_('Choose people who have been source to this acquisition'),
        verbose_name=_('Source'))
    dealer = models.ManyToManyField(
        Person,
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
