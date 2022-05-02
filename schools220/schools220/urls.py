from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from schools220.api import router

urlpatterns = []

urlpatterns += i18n_patterns(
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('schoolsite220.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
