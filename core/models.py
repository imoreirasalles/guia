from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import HStoreField
import uuid


class Collection(models.Model):
    uuid     = models.UUIDField(default=uuid.uuid4, max_length=32, editable=False, unique=True)
    id_old   = HStoreField(null=True, blank=True)
    title    = models.CharField(max_length=250, null=False)
    slug     = models.CharField(max_length=60, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
