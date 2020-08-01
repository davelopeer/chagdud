from django.urls import path
from khadro_ling.views import KhadroLingHomeView, KhadroLingAboutUsView


app_name = 'khadroling'

urlpatterns = [
    path('', KhadroLingHomeView.as_view(), name='home'),
    path('quem-somos', KhadroLingAboutUsView.as_view(), name='about-us'),
]
