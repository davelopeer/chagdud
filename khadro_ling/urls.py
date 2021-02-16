from django.urls import path
from khadro_ling.views import HomeView, AboutUsView

from offering.views import offerings_view

app_name = 'khadroling'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('quem-somos/', AboutUsView.as_view(), name='about-us'),
]
