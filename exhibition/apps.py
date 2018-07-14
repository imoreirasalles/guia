from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExhibitionConfig(AppConfig):
    name = 'exhibition'
    verbose_name = _('Exhibition App')
