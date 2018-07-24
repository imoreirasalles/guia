from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LocationConfig(AppConfig):
    name = 'location'
    verbose_name = _('Location App')
