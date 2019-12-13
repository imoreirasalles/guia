from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VocabularyConfig(AppConfig):
    name = 'vocabulary'
    verbose_name = _('Vocabulary')
