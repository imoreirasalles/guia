# Django core imports
from django.db import models
# Third part imports
import uuid
# Imports from guia project
from collection.models import *


class Person(models.Model):
    """
    Person Class used to record info about partners, authors, organizations, etc
    """
    uuid = models.UUIDField(default=uuid.uuid4, max_length=32, editable=False, unique=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    nickname = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    # thumbnail = models.ForeignKey(Thumbnail, null=True, blank=True,  on_delete=models.SET_NULL)
    abstract = models.TextField(null=True, blank=True)
    full_text = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.slug
