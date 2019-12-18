from django.urls import (
    path, include, re_path
)
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView
)

from . import views

app_name = "api"

urlpatterns = [
    path(
        '',
        views.SchemaView.with_ui('redoc', cache_timeout=0),
        name='documentation'
    ),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # include urls api, example:
    # path('example/', include('apps.example.urls')),
]
