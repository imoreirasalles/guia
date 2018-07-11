from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Third part imports
import uuid

# Project Apps Imports
from django.apps import apps


class PublicationType(models.Model):
    """Used to label type of publications"""
    created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Auto set field'),
        verbose_name=_('Created in'))
    title = models.CharField(
        max_length=256,
        help_text=_('Ex.: book'),
        verbose_name=_('Title'))
    description = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_('Ex.: A book is...'),
        verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Publication Type')
        verbose_name_plural=_('Publication Types')


class Publication(models.Model):
    """To store data about publications"""
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
        help_text=_('Institucional Collection Human Identifier'),
        verbose_name=_('ID'))
    title = models.CharField(
        default=_('No title publication'),
        max_length=256,
        help_text=_('Ex.: The complete photo collection of Sebastião Salgado.'),
        verbose_name=_('Title'))
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Ex.: book-sebastiao-salgado'),
        verbose_name=_('Slug'))
    type = models.ForeignKey(
        PublicationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the more appropriate type to means this publication'),
        verbose_name=_('Type'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This publication is composed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: The book serie is...'),
        verbose_name=_('Full Text'))
    author = models.ManyToManyField(
        'person.Person',
        related_name='personAuthor',
        blank=True,
        help_text=_("Choose some collection's authors"),
        verbose_name=_('Authors'))
    date_released = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose the released date'),
        verbose_name=_('Released Date'))
    publisher = models.ManyToManyField(
        'person.Person',
        related_name='personPublisher',
        blank=True,
        help_text=_("Choose some collection's authors"),
        verbose_name=_('Authors'))
    dimension = JSONField(
        null=True,
        blank=True,
        help_text=_('Feed with information about dimensions'),
        verbose_name=_('Dimensions'))
    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total number of pages'),
        verbose_name=_('Number of pages'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this publication'),
        verbose_name=_('Other Data'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Publication')
        verbose_name_plural=_('Publications')
