import uuid
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class BaseModel(models.Model):

    class Meta:
        abstract = True

    """Used to base models with uuid, """
    id = models.BigAutoField(
        primary_key=True,
        editable=False,
        help_text=_('Sequential identifier'),
        verbose_name=_('ID'))
    uuid = models.UUIDField(
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('Universal unique identifier'),
        verbose_name=_('UUID'))
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('Date this resource was created'),
        verbose_name=_('Created at'),
        editable=False)
    updated_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('Date this resource was last updated'),
        verbose_name=_('Updated at'),
        editable=False)
    label = models.CharField(
        default=None,
        null=True,
        blank=False,
        max_length=128,
        help_text=_('Short title for this resource'),
        verbose_name=_('Label'))
    summary = models.TextField(
        default=None,
        null=True,
        blank=True,
        max_length=512,
        help_text=_('Brief description'),
        verbose_name=_('Summary'))
    published = models.BooleanField(
        default=False,
        db_index=True,
        help_text=_('This resource is available to the public'),
        verbose_name=_('Published'))
    extra = JSONField(
        null=True,
        blank=True,
        help_text=_('Semi-structured data in JSON'),
        verbose_name=_('Extra'))
    slug = models.SlugField(
        default=None,
        max_length=128,
        unique=True,
        null=True,
        blank=True,
        editable=False,
        help_text=_('String presented as part of the URL'),
        verbose_name=_('Slug'))

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):

        # Slugify UUID
        if self.slug != self.uuid:
            self.slug = slugify(self.uuid)

        # Update date
        if self.updated_at:
            self.updated_at = timezone.now()

        return super().save(*args, **kwargs)
