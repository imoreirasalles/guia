from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GlossaryConfig(AppConfig):
    name = 'glossary'
    verbose_name = _('Glossary App')
