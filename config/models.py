import uuid
from datetime import datetime
from django.db import models
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
        default=datetime.now,
        help_text=_('Auto set field'),
        verbose_name=_('Created at'),
        editable=False)
    updated_at = models.DateTimeField(
        default=datetime.now,
        help_text=_('Auto set field'),
        verbose_name=_('Updated at'),
        editable=False)
    label = models.CharField(
        default=None,
        null=True,
        blank=False,
        max_length=128,
        help_text=_('Short title'),
        verbose_name=_('Label'))
    summary = models.CharField(
        default=None,
        null=True,
        blank=True,
        max_length=512,
        help_text=_('Brief description'),
        verbose_name=_('Summary'))
    published = models.BooleanField(
        default=False,
        db_index=True,
        help_text=_('False by default'),
        verbose_name=_('Published'))
    extra = JSONField(
        null=True,
        blank=True,
        help_text=_('Semi-structured data'),
        verbose_name=_('Extra'))
    slug = models.SlugField(
        default=None,
        max_length=128,
        unique=True,
        null=True,
        blank=True,
        editable=False,
        help_text=_('Generated based on UUID'),
        verbose_name=_('Slug'))
