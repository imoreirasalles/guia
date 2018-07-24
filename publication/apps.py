from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PublicationConfig(AppConfig):
    name = 'publication'
    verbose_name = _('Publication App')
