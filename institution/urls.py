from django.urls import path
from institution.views import HomeView, AboutUsView

app_name = 'institution'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('quem-somos', AboutUsView.as_view(), name='about-us')
]
