from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
import reversion


@reversion.register()
class Location(models.Model):
    """store places addresses, and link places with art works, sets, collection, persons, etc"""
    title = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text=_('Ex.: Title of place - House of Photographer Smith'),
        verbose_name=_('Title'))
    street = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text=_('Ex.: Main Avenue'),
        verbose_name=_('Street'))
    number = models.CharField(
        max_length=32,
        null=False,
        blank=True,
        help_text=_('Ex.: 1580'),
        verbose_name=_('Number'))
    complement = models.CharField(
        max_length=128,
        null=False,
        blank=True,
        help_text=_('Ex.: Apartament 2B'),
        verbose_name=_('Complement'))
    neighborhood = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text=_('Ex: Exhibition Vile'),
        verbose_name=_('Neighborhood'))
    state = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text=_('Ex.: New York'),
        verbose_name=_('State'))
    city = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text=_('Ex.: New York City'),
        verbose_name=_('City'))
    country = models.CharField(
        max_length=64,
        null=False,
        blank=True,
        help_text=_('Ex.: United States of America'),
        verbose_name=_('Country'))
    postal_code = models.CharField(
        max_length=32,
        null=False,
        blank=True,
        help_text=_('Ex.: 434093-4085485'),
        verbose_name=_('Postal Code'))
    lat_and_long = models.PointField(
        null=False,
        blank=True,
        help_text=_('Ex.: latitude 438974592318, longitude 9482375732'),
        verbose_name=_('Latitude & Longitude'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_('Place')
        verbose_name_plural = _('Places')
