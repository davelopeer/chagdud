from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('institution.urls')),
    path('khadroling/', include('khadro_ling.urls'))
]
