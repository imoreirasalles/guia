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
class Person(Base):
    """
    Person Class used to record info about partners, authors, organizations, etc
    """
    id_human = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    person_type = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        help_text=_('Choose the more appropriate option'),
        verbose_name=_('Person Type'))
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
        verbose_name=_('Authority Member'))
    gender = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        help_text=_('Biological sex gender'),
        verbose_name=_('Gender'))
    # nation_origin =
    # nation_main =
    capture = models.ManyToManyField(
        'digitalassetsmanagement.Capture',
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Captures'))
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
