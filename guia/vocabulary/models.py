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

    semantic_url = models.URLField(
        default=None,
        null=True,
        blank=True,
        max_length=200,
        help_text=_('https://www.wikidata.org/wiki/Q3180571'),
        verbose_name=_('Semantic URL'))

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

    terms = models.ManyToManyField(
        Term,
        blank=True,
        related_name='terms')


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