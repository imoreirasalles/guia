from django.db import models


class ManagementUnit(models.Model):
    """Used to store unit of institutional management"""
    title = models.CharField(max_length=128, null=False, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
