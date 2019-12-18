DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Улучшенный поиск в админке
    'djangoql',
    # Импорт и экспорт в админке из/в файл(а)
    'import_export',
    # Добавляет Cross-Origin Resource Sharing (CORS) заголовки
    'corsheaders',
    # Теги для добавления стилий формам
    'widget_tweaks',
    # REST API
    'rest_framework',
    # Документация REST API
    'drf_yasg',
    # Удаляет файлы при удалении их в ImageField и FileField
    'django_cleanup.apps.CleanupConfig',
    # Загрузчик webpack
    'webpack_loader',

    # Пользовательские настройки из панели администратора
    'constance',
    'constance.backends.database',

    # SQL запросы из админки
    'explorer',
    # Различные утилиты
    'etc',
]

PROJECT_APPS = [
    'apps.utils.apps.UtilsConfig',
    'apps.main.apps.MainConfig',
    'apps.api.apps.ApiConfig',
    'apps.info.apps.InfoConfig',

]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    'django_extensions',
    *PROJECT_APPS,
    'debug_toolbar',
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
