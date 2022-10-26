from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pcus_list.views import PCUSModelViewSet, OBJModelViewSet

router = DefaultRouter()
router.register('objects', OBJModelViewSet)
router.register('pcus', PCUSModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('pcus_list.urls')),
    path('zvk/', include('zvk_getter.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)