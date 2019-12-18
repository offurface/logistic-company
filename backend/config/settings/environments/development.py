import os

from ..components import (
    PUBLIC_DIR,
    DEVELOPER_APPS,
    DEVELOPER_MIDDLEWARE
)

INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    *DEVELOPER_APPS
]

MIDDLEWARE = [
    *DEVELOPER_MIDDLEWARE
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            PUBLIC_DIR, 'db.sqlite3'
        ),
        'TEST': {
            'NAME': os.path.join(
                PUBLIC_DIR, 'test_db.sqlite3'
            ),
        },
    },
}
