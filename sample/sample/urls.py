from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 # admin app
    path(r'admin/', admin.site.urls),
 # Cuisine app
    path(r'cuisine/', include(('cuisine.urls', 'cuisine'))),]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

