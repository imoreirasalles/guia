from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CollectionConfig(AppConfig):
    name = 'collection'
    verbose_name = _('Collection App')
