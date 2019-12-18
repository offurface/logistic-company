from ..components import (
    env,
    PRODUCTION_APPS,
    PRODUCTION_MIDDLEWARE
)

ALLOWED_HOSTS = [
    env('SITE_DOMAIN'),
]

INSTALLED_APPS = [
    *PRODUCTION_APPS,
]

MIDDLEWARE = [
    *PRODUCTION_MIDDLEWARE,
]

DATABASES = {
    'default': env.db(),
}
