import os
import random

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a Django app directory structure for the given app name in the apps directory.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dev', default=False, action='store_true',
            help='Generate unique name file'
        )

    def get_example_env(self):
        path_example = os.path.join(settings.PROJECT_DIR, '.env.example')
        example = open(path_example, "r")
        return example.read()

    def get_secret_key(self):
        return "".join([
            random.choice(
                "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
            ) for i in range(50)
        ])

    def create_env_file(self, content):
        path = os.path.join(settings.PROJECT_DIR, '.env')
        if not os.path.exists(path):
            env = open(path,"w+")
            env.write(content)
            env.close()

    def handle(self, *args, **options):
        content = self.get_example_env()
        secret_key = self.get_secret_key()

        if "SECRET_KEY" not in content:
            content = content + f"\nSECRET_KEY='{secret_key}'\n"
        else:
            content = content.replace("SECRET_KEY=''", f"SECRET_KEY='{secret_key}'")

        self.create_env_file(content)
