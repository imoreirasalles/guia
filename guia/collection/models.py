from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


from config.models import BaseModel
from django.apps import apps



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
    article = models.TextField(
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
    inventory_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the last inventory was completed?'),
        verbose_name=_('Inventory date'))
    insurance_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any insurance?'),
        verbose_name=_('Insurance'))
    insurance_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the last insurance was signed?'),
        verbose_name=_('Insurance date'))
    contract_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any contract?'),
        verbose_name=_('Contract'))
    contract_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the last contract was signed?'),
        verbose_name=_('Contract date'))
    aggregation_type = models.ForeignKey(
        'vocabulary.Term',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('Select the aggregation type'),
        verbose_name=_('Aggregation Type'))
    

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'uuid': self.uuid})

    def save(self, *args, **kwargs):

        # Slugify UUID
        if self.slug != self.uuid:
            self.slug = slugify(self.uuid)

        # Update date
        if self.updated_at:
            self.updated_at = timezone.now()

        return super().save(*args, **kwargs)
