from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from guia.models import Base, DraftModel
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# Third part imports
import reversion

# Project Apps Imports
from django.apps import apps


@reversion.register()
class EventType(Base):
    """Used to label events according type"""
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


@reversion.register()
class Event(Base, DraftModel):
    """Used to archive events promoted by the institution"""
    id_human = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
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
        'location.Location',
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
    docs = models.ManyToManyField(
        'digitalassetsmanagement.Doc',
        blank=True,
        verbose_name=_('Documents'))
    audience = models.IntegerField(
        verbose_name=_('Audience'),
        blank=True,
        null=True,
        help_text=_("Number of participants"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug != None:
            return reverse('event_detail_slug', kwargs={'slug': self.slug})
        else:
            return reverse('event_detail', kwargs={'pk': self.id_auto_series})

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            super(Event, self).save(*args, **kwargs)
        if self.title == None:
            title_str = "[no-title]"
        else:
            title_str = self.title

        slug_auto = slugify(str(self.id_auto_series) +
                            '_event_' +
                            str(title_str))

        self.slug = slug_auto
        super(Event, self).save(*args, **kwargs)

    class Meta:
        verbose_name=_('Event')
        verbose_name_plural=_('Events')
