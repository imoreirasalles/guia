from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from guia.models import Base
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# Third part imports
import reversion

# Project Apps Imports
from django.apps import apps


@reversion.register()
class PublicationType(Base):
    """Used to label type of publications"""
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


@reversion.register()
class Publication(Base):
    """To store data about publications"""
    id_human = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    type = models.ForeignKey(
        PublicationType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the more appropriate type to means this publication'),
        verbose_name=_('Type'))
    capture = models.ManyToManyField(
        'digitalassetsmanagement.Capture',
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Captures'))        
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
        help_text=_("Choose some Author(s)"),
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
        help_text=_("Choose some Publisher"),
        verbose_name=_('Publisher(s)'))
    dimension = JSONField(
        null=True,
        blank=True,
        help_text=_('Feed with information about dimensions'),
        verbose_name=_('Dimensions'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this publication'),
        verbose_name=_('Other Data'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug != None:
            return reverse('publication_detail_slug', kwargs={'slug': self.slug})
        else:
            return reverse('publication_detail', kwargs={'pk': self.id_auto_series})

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            super(Publication, self).save(*args, **kwargs)
        if self.title == None:
            title_str = "[no-title]"
        else:
            title_str = self.title


        slug_auto = slugify(str(self.id_auto_series) + '_' +
                            'publication_' +
                            str(title_str))
        self.slug = slug_auto
        super(Publication, self).save(*args, **kwargs)

    class Meta:
        verbose_name=_('Publication')
        verbose_name_plural=_('Publications')
