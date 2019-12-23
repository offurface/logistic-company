from django.urls import path, include, re_path
from django.middleware import locale
from . import views


urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('info/', include('apps.info.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:template>/', views.PageLoaderView.as_view(), name='page'),
]
