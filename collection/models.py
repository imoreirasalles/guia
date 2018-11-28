from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models
from guia.models import Base, DraftModel
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# Third part imports
import reversion
from reversion.models import *
# Project Apps Imports
from django.apps import apps


@reversion.register()
class Container(Base):
    """Used to store an aggroupment of items"""
    id_human = models.CharField(
        default=None,
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    aggregation_type = models.ForeignKey(
        'glossary.AggregationType',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Container Aggregation Type'),
        verbose_name=_('Aggregation Type'))
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This container is...'),
        verbose_name=_('Full Description'))
    items = models.ManyToManyField(
        'digitalassetsmanagement.Item',
        blank=True,
        help_text=_('Itens that composes the container'),
        verbose_name=_('Items'))
    description_level = models.ForeignKey(
        'glossary.DescriptionLevel',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose a description level to this container'),
        verbose_name=_('Description level'))
    container_child = models.ManyToManyField(
        'self',
        blank=True,
        help_text=_('Choose child containers to aggregate to this one'),
        verbose_name=_('Child containers'))

    def __str__(self):
        if self.title == None:
            Container_str = str(self.uuid)
        elif self.aggregation_type != None:
            Container_str = str(self.aggregation_type) + str(': ') + str(self.title)
        else:
            Container_str = _('No type: ') + self.title
        return Container_str

    def get_date_created(self):
        return Version.objects.get_for_object(self).order_by("id").first().revision.date_created

    def get_absolute_url(self):
        if self.slug != None:
            return reverse('container_detail_slug', kwargs={'slug': self.slug})
        else:
            return reverse('container_detail', kwargs={'pk': self.id_auto_series})

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            super(Container, self).save(*args, **kwargs)
        if self.aggregation_type == None:
            aggregation_type_str = "[no-aggregation]"
        else:
            aggregation_type_str = self.aggregation_type

        slug_auto = slugify(str(aggregation_type_str) + '-' +
                            str(self.id_auto_series) + '-' +
                            self.title)
        self.slug = slug_auto
        super(Container, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Container')
        verbose_name_plural = _('Containers')


@reversion.register()
class Collection(Base, DraftModel):
    """
    Main class of collection
    """
    id_human = models.CharField(
        default=None,
        max_length=64,
        null=True,
        blank=True,
        unique=True,
        help_text=_('Institucional Identifier'),
        verbose_name=_('Institucional ID'))
    id_old = JSONField(
        default=None,
        null=True,
        blank=True,
        help_text=_('Legacy Identifiers'),
        verbose_name=_('Old IDs'))
    abstract = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: This collection is composed by...'),
        verbose_name=_('Abstract'))
    full_text = models.TextField(
        null=True,
        blank=True,
        help_text=_('Ex.: All itens in this collection...'),
        verbose_name=_('Full Text'))
    description_level = models.ForeignKey(
        'glossary.DescriptionLevel',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose an Option'),
        verbose_name=_('Description Level'))
    aggregation_type = models.ForeignKey(
        'glossary.AggregationType',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose an Option'),
        verbose_name=_('Aggregation Type'))
    genre_tags = models.ManyToManyField(
        'glossary.GenreTag',
        blank=True,
        help_text=_('Choose one or more options'),
        verbose_name=_('Genre Tags'))
    dimensions = JSONField(
        null=True,
        blank=True,
        help_text=_('Feed with information about dimensions'),
        verbose_name=_('Dimensions'))
    date_start = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    date_start_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Choose a start date caption'),
        verbose_name=_('Initial date caption'))
    date_end = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date'),
        verbose_name=_('Final date'))
    date_end_caption = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Choose a final date caption'),
        verbose_name=_('Final date caption'))
    capture = models.ManyToManyField(
        'digitalassetsmanagement.capture',
        blank=True,
        help_text=_('Choose some introduction and representative images'),
        verbose_name=_('Image'))
    author = models.ManyToManyField(
        'person.Person',
        related_name='collection_author',
        blank=True,
        help_text=_("Choose some collection's authors"),
        verbose_name=_('Authors'))
    container = models.ManyToManyField(
        Container,
        blank=True,
        help_text=_('Choose containers that compose the collection'),
        verbose_name=_('Containers'))
    items_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total collection items'),
        verbose_name=_('Total Items'))
    items_processed = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total processed items'),
        verbose_name=_('Processed Items'))
    items_online = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total online collection items'),
        verbose_name=_('Online Items'))
    access_condition = models.ForeignKey(
        'glossary.AccessCondition',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Choose the more appropriate access condition to this collection'),
        verbose_name=_('Access Condition'))
    access_local_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('Is there any local access to the collection?'),
        verbose_name=_('Local Access Status'))
    access_online_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('Is there any online access to the collection?'),
        verbose_name=_('Online Access Status'))
    access_link = models.URLField(
        null=True,
        blank=True,
        help_text=_('Do you have some online link access to this collection?'),
        verbose_name=_('Access Link'))
    location_generic = models.ForeignKey(
        'location.Location',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('What is the generic location to the collection?'),
        verbose_name=_('Generic Location'))
    location_specific = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_('What is the specific location to this collection?'),
        verbose_name=_('Specific Location'))
    inventary_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('Is there any inventary to this collection?'),
        verbose_name=_('Inventary Status'))
    inventary_last_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('What is the inventary last date?'),
        verbose_name=_('Inventary Last Date'))
    inventary_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Several data about the inventary'),
        verbose_name=_('Inventary Data'))
    management_unit = models.ForeignKey(
        'management.ManagementUnit',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('What is the management unit concerning to this collection?'),
        verbose_name=_('Management Unit'))
    other_data = JSONField(
        null=True,
        blank=True,
        help_text=_('Other unstructured data of this collection'),
        verbose_name=_('Other Data'))
    docs = models.ManyToManyField(
        'digitalassetsmanagement.Doc',
        blank=True,
        verbose_name=_('Documents'))

    def __str__(self):
        if self.title == None:
            collection_str = str(self.uuid)
        elif self.aggregation_type != None:
            collection_str = str(self.aggregation_type) + str(': ') + str(self.title)
        else:
            collection_str = _('No type: ') + self.title
        return collection_str

    def get_absolute_url(self):
        if self.slug != None:
            return reverse('collection_detail_slug', kwargs={'slug': self.slug})
        else:
            return reverse('collection_detail', kwargs={'pk': self.id_auto_series})

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            super(Collection, self).save(*args, **kwargs)
        if self.aggregation_type == None:
            aggregation_type_str = "[no-aggregation]"
        else:
            aggregation_type_str = self.aggregation_type
        if self.title == None:
            title_str = "[no-title]"
        else:
            title_str = self.title

        slug_auto = slugify(str(self.id_auto_series) + '-' +
                            str(aggregation_type_str) + '-' +
                            str(title_str))
        self.slug = slug_auto
        super(Collection, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')
