from .env import env

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = env('EMAIL_HOST', default='localhost')
EMAIL_PORT = env('EMAIL_PORT', default=25)
EMAIL_HOST_USER = env('EMAIL_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD', default='')
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = ''
SERVER_EMAIL = env('EMAIL_NAME', default='root@localhost')
DEFAULT_FROM_EMAIL = env('EMAIL_NAME', default='webmaster@localhost')
MANAGERS = [
    (
        'Manager',
        env('EMAIL_MANAGER', default='manager@localhost')
    ),
]
