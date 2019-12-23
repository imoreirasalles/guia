from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


from config.models import BaseModel


class Term(BaseModel):

    """
    Main class of Term
    """

    class Meta:
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')

    id_human = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=32,
        help_text=_('Human readable identifier'),
        verbose_name=_('Identifier'))

    semantic_url = models.URLField(
        default=None,
        null=True,
        blank=True,
        max_length=200,
        help_text=_('https://www.wikidata.org/wiki/Q3180571'),
        verbose_name=_('Semantic URL'))


class Vocabulary(BaseModel):

    """
    Main class of List of Terms
    """

    class Meta:
        verbose_name = _('Vocabulary')
        verbose_name_plural = _('Vocabularies')

    id_human = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=32,
        help_text=_('Human readable identifier'),
        verbose_name=_('Identifier'))

    semantic_url = models.URLField(
        default=None,
        null=True,
        blank=True,
        max_length=200,
        help_text=_('https://www.wikidata.org/wiki/Q3180571'),
        verbose_name=_('Semantic URL'))

    terms = models.ManyToManyField(
        Term,
        blank=True,
        related_name='vocabularies',
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Terms'))
