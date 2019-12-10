from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse
from datetime import datetime


from config.models import BaseModel


class Collection(BaseModel):
    identifier = models.CharField(
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

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('collection_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uuid)

        return super().save(*args, **kwargs)
