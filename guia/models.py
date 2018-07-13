from django.db import models
from django.utils.translation import gettext_lazy as _

# Third part imports
import uuid


class Base(models.Model):
    """Used to base models with uuid, """
    id_auto_series = models.BigAutoField(
        primary_key=True,
        editable=False,
        help_text=_('Auto Increment ID'),
        verbose_name=_('ID'))
    uuid = models.UUIDField(
        default=uuid.uuid4,
        max_length=32,
        editable=False,
        unique=True,
        help_text=_('This is an auto set field'),
        verbose_name=_('Universal Unique Identifier'))

    class Meta:
        abstract = True
