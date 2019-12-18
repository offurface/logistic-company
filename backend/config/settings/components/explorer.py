EXPLORER_CONNECTIONS = {
    'Default': 'default'
}
EXPLORER_DEFAULT_CONNECTION = 'default'

EXPLORER_PERMISSION_VIEW = lambda u: u.is_staff
EXPLORER_PERMISSION_CHANGE = lambda u: u.is_superuser

EXPLORER_SCHEMA_EXCLUDE_TABLE_PREFIXES = (
    'jet',
    'django',
    'explorer',
    'dashboard',
)
