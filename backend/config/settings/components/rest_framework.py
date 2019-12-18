REST_FRAMEWORK  = {
    'DEFAULT_PERMISSION_CLASSES' : (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework_simplejwt.authentication.JWTAuthentication' ,
    )
}

SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,

    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': settings.SECRET_KEY,
    # 'VERIFYING_KEY': None,
}
