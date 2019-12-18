from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    name = 'apps.main'
    verbose_name = _('Главное')
