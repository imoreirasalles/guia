from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _

# Third part imports
import uuid

# Project guia imports
from location.models import *


class EventType(models.Model):
    """Used to label events according type"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: course, workshop, show, launching'),
        verbose_name=_('Title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('Ex.: A course is a formative event... '),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Event Type')
        verbose_name_plural=_('Events Type')


class Event(models.Model):
    """Used to archive events promoted by the institution"""
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
        help_text=_('Ex.: Launch of new publication...'),
        verbose_name=_('Title'))
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Ex.: lauch-new-publication'),
        verbose_name=_('Slug'))
    date_start = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    date_end = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date'),
        verbose_name=_('Final date'))
    type = models.ForeignKey(
        EventType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the an appropriate type to this one'),
        verbose_name=_('Type'))
    location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the location where this event occurs'),
        verbose_name=_('Location'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This event was performed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: The course was...'),
        verbose_name=_('Full Text'))
    team = JSONField(
        null=True,
        blank=True,
        help_text=_('Feed with information about team that worked on this'),
        verbose_name=_('Team'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this collection'),
        verbose_name=_('Other Data'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Event')
        verbose_name_plural=_('Events')
