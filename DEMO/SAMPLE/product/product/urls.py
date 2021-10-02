from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # admin app
    path(r'admin/', admin.site.urls
         ),
    # Cuisine app
    path(r'mobile/', include(('mobile.urls', 'mobile')
                              )
         ),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
