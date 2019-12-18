from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('', views.HomeView.as_view(), name='home'),
    path('<slug:template>/', views.PageLoaderView.as_view(), name='page'),
]
