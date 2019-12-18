import os

CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BACKEND_DIR = os.path.dirname(CONFIG_DIR)
PROJECT_DIR = os.path.dirname(BACKEND_DIR)

APPS_DIR = os.path.join(BACKEND_DIR, 'apps')
PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')
LOGS_DIR = os.path.join(PROJECT_DIR, 'logs')
FIXTURES_DIR = os.path.join(BACKEND_DIR, 'fixtures')

STATIC_DIR = os.path.join(PUBLIC_DIR, 'static')
MEDIA_DIR = os.path.join(PUBLIC_DIR, 'media')
FRONTEND_DIR = os.path.join(PROJECT_DIR, 'frontend')
TEMPLATES_DIR = os.path.join(FRONTEND_DIR, 'templates')

FIXTURE_DIRS = [FIXTURES_DIR, ]
