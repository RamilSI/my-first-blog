from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite import settings
from report.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('report/', include('report.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, documents_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
