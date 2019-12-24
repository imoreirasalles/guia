from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
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
    items_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total of collection individual items'),
        verbose_name=_('Total of items'))
    linear_meters = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_('Total of linear meters occupied by the collection'),
        verbose_name=_('Linear meters'))
    progress_technical = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        null=True,
        blank=True,
        help_text=_('Percentage of items available to researchers'),
        verbose_name=_('Technical progress'))
    progress_online = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        null=True,
        blank=True,
        help_text=_('Percentage of items available online'),
        verbose_name=_('Online progress'))
    inventory_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any inventory?'),
        verbose_name=_('Inventory'))
    inventory_start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the inventory beggins?'),
        verbose_name=_('Inventory start'))
    inventory_end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the inventory ends?'),
        verbose_name=_('Inventory end'))
    insurance_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any insurance?'),
        verbose_name=_('Insurance'))
    insurance_start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the insurance beggins?'),
        verbose_name=_('Insurance start'))
    insurance_end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the insurance ends?'),
        verbose_name=_('Insurance end'))
    contract_status = models.NullBooleanField(
        null=True,
        blank=True,
        help_text=_('This collection has any contract?'),
        verbose_name=_('Contract'))
    contract_start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the contract beggins?'),
        verbose_name=_('Contract start'))
    contract_end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('When the contract ends?'),
        verbose_name=_('Contract end'))
    private_notes = models.TextField(
        default=None,
        null=True,
        blank=True,
        help_text=_('Administrative information not publicly available'),
        verbose_name=_('Private notes'))
    management_team = models.ForeignKey(
        Term,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='management_teams',
        limit_choices_to={'vocabularies__id_human': 'management_team'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Management Team'))
    management_storage = models.ManyToManyField(
        Term,
        blank=True,
        related_name='management_storages',
        limit_choices_to={'vocabularies__id_human': 'management_storage'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Management Storage'))
    aggregation_type = models.ManyToManyField(
        Term,
        blank=True,
        related_name='aggregation_types',
        limit_choices_to={'vocabularies__id_human': 'aggregation_type'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Aggregation Type'))
    acquisition_type = models.ForeignKey(
        Term,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='acquisition_types',
        limit_choices_to={'vocabularies__id_human': 'acquisition_type'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Acquisition Type'))
    restriction_type = models.ManyToManyField(
        Term,
        blank=True,
        related_name='restriction_types',
        limit_choices_to={'vocabularies__id_human': 'restriction_type'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Access Restrictions'))
    items_type = models.ManyToManyField(
        Term,
        blank=True,
        related_name='items_types',
        limit_choices_to={'vocabularies__id_human': 'items_type'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Resource Types'))
    language_type = models.ManyToManyField(
        Term,
        blank=True,
        related_name='language_types',
        limit_choices_to={'vocabularies__id_human': 'language_type'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Languages'))
    featured_people = models.ManyToManyField(
        Term,
        blank=True,
        related_name='featured_peoples',
        limit_choices_to={'vocabularies__id_human': 'featured_people'},
        help_text=_('Select the terms used in this vocabulary'),
        verbose_name=_('Featured People'))

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'uuid': self.uuid})
