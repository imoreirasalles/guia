from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PersonConfig(AppConfig):
    name = 'person'
    verbose_name = _('Person App')
