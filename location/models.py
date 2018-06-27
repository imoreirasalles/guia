from django.db import models
from django.contrib.gis.db import models

class Location(models.Model):
    """store places addresses, and link places with art works, sets, collection, persons, etc"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128, null=False, blank=True)
    street = models.CharField(max_length=128, null=False, blank=True)
    number = models.CharField(max_length=32, null=False, blank=True)
    complement = models.CharField(max_length=128, null=False, blank=True)
    neighborhood = models.CharField(max_length=64, null=False, blank=True)
    state = models.CharField(max_length=64, null=False, blank=True)
    city = models.CharField(max_length=64, null=False, blank=True)
    country = models.CharField(max_length=64, null=False, blank=True)
    postal_code = models.CharField(max_length=32, null=False, blank=True)
    lat_and_long = models.PointField(null=False, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Locais"
