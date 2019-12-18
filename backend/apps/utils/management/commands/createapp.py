import os

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a Django app directory structure for the given app name in the apps directory.'

    def add_arguments(self, parser):
        parser.add_argument(
            'name', type=str,
            help='Name of the application or project'
        )

    def handle(self, *args, **options):
        name = options['name']
        path = os.path.join(settings.APPS_DIR, name)
        if not os.path.exists(path):
            os.mkdir(path)
        management.call_command("startapp", name, path)
