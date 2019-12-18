from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


admin.site.site_header = _("Панель управления")
admin.site.index_title = _("Панель управления")
admin.site.site_title = _("Администрирование")


urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('sql/', include('explorer.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('apps.main.urls')),
]


urlpatterns = static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + i18n_patterns(
    *urlpatterns,
    prefix_default_language=False,
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
