# Django core imports
from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Third part imports
import uuid
import reversion
# Project guia imports
from django.apps import apps


@reversion.register()
class Person(models.Model):
    """
    Person Class used to record info about partners, authors, organizations, etc
    """
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
        help_text=_('Institucional Human Identifier'),
        verbose_name=_('ID'))
    person_type = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        help_text=_('Choose the more appropriate option'),
        verbose_name=_('Person Type'))
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: Mr. Louis-Jacques-Mandé Daguerre'),
        verbose_name=_('Title'))
    title_index = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('Ex.: DAGUERRE, Louis-Jacques-Mandé.'),
        verbose_name=_('Title Index'))
    is_staff = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This person is a staff member?'),
        verbose_name=_('Staff Member'))
    is_partner = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This person is an institucional partner?'),
        verbose_name=_('Institutional Partner'))
    is_feature = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This is a featured person?'),
        verbose_name=_('Staff Member'))
    gender = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        help_text=_('Biological sex gender'),
        verbose_name=_('Gender'))
    # nation_origin =
    # nation_main =
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Ex.: the-photographer-sebastiao-salgado'),
        verbose_name=_('Slug'))
    thumbnail = models.ManyToManyField(
        'digitalassetsmanagement.Thumbnail',
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Thumbnails'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This person is...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: The photographer...'),
        verbose_name=_('Full Text'))
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
    url = models.URLField(
        null=True,
        blank=True,
        help_text=_('Representative URL about this person'),
        verbose_name=_('URL'))
    linked_open_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Ex.: VIAF, ULAN, Wiki Data, etc'),
        verbose_name=_('Linked Open Data Dictionary'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
