from django.db import models
from django.contrib import admin


class Collection(models.Model):
    title =  models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.title
