import os

from .paths import (
    FRONTEND_DIR, STATIC_DIR, MEDIA_DIR
)

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR

STATICFILES_DIRS = [
    os.path.join(FRONTEND_DIR, 'static'),
]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(
            FRONTEND_DIR, 'static', 'dist', 'webpack-stats.json'
        ),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
