from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('institution.urls')),
    path('khadroling/', include('khadro_ling.urls'))
]

# In the development server you may serve the user uploaded files (media) 
# using django.contrib.staticfiles.views.serve() view
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
