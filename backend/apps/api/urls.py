from django.urls import (
    path, include, re_path
)

from . import views

app_name = "api"

urlpatterns = [
    path(
        '',
        views.SchemaView.with_ui('redoc', cache_timeout=0),
        name='documentation'
    ),
]
