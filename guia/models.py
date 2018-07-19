from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from django.utils.translation import pgettext_lazy
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db import IntegrityError
from django.shortcuts import render_to_response
# Third part imports
import uuid

# Project Apps Imports
from django.apps import apps


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
    title = models.CharField(
        default=_(' '),
        max_length=256,
        help_text=_('Ex.: The title of this record'),
        verbose_name=_('Title'))
    slug = models.SlugField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
        help_text=_('Ex.: complete-collection-sebastiao-salgado'),
        verbose_name=_('Slug'))

    def save(self, *args, **kwargs):
        if self.id_auto_series == None:
            slug_auto = slugify( self.title + ' ' + str(uuid.uuid4()) )
        else:
            slug_auto = slugify( str(self.id_auto_series) + '_' + self.title)

        self.slug = slug_auto
        super(Base, self).save(*args, **kwargs)


    class Meta:
        abstract = True



    # def save(self, *args, **kwargs):
    #     slug_auto = slugify( str(self.id_auto_series) + self.title)
    #     self.slug = slug_auto
    #     test = False
    #     while test == False:
    #         try:
    #             super(Base, self).save(*args, **kwargs)
    #         except IntegrityError:
    #             slug_auto = slugify( '01_' + str(self.id_auto_series) + self.title)
    #             self.slug = slug_auto
    #             super(Base, self).save(*args, **kwargs)
    #         else:
    #             test = True
    #             super(Base, self).save(*args, **kwargs)
