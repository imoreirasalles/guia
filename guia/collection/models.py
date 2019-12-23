from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils import timezone


from config.models import BaseModel
from vocabulary.models import Term
from django.apps import apps


from ckeditor.fields import RichTextField


class Collection(BaseModel):

    """
    Main class of Collection
    """

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    id_human = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=32,
        help_text=_('Human readable identifier'),
        verbose_name=_('Identifier'))
    article = RichTextField(
        null=True,
        blank=True,
        help_text=_('Full description'),
        verbose_name=_('Article'))
    start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose a start date'),
        verbose_name=_('Initial Date'))
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('Choose an final date'),
        verbose_name=_('Final date'))
    dimention_items = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total collection items'),
        verbose_name=_('Total of items'))
    progressbar_work = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Percentage of work done'),
        verbose_name=_('Work progress bar'))
    progressbar_online = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Percentage of work available online'),
        verbose_name=_('Online progress bar'))
    inventory_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any inventory?'),
        verbose_name=_('Inventory'))
    inventory_start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the inventory beggins?'),
        verbose_name=_('Inventory start date'))
    inventory_end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the inventory ends?'),
        verbose_name=_('Inventory end date'))
    insurance_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any insurance?'),
        verbose_name=_('Insurance'))
    insurance_start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the insurance beggins?'),
        verbose_name=_('Insurance start date'))
    insurance_end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the insurance ends?'),
        verbose_name=_('Insurance end date'))
    contract_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any contract?'),
        verbose_name=_('Contract'))
    contract_start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the contract beggins?'),
        verbose_name=_('Contract start date'))
    contract_end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the contract ends?'),
        verbose_name=_('Contract end date'))
    aggregation_type = models.ManyToManyField(
        Term,
        blank=True,
        related_name='aggregation_types',
        limit_choices_to={'vocabularies__id_human': 'aggregation_type'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Aggregation Type'))

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'uuid': self.uuid})
