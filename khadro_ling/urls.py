from django.urls import path
from khadro_ling.views import KhadroLingHomeView


app_name = 'khadroling'

urlpatterns = [
    path('', KhadroLingHomeView.as_view(), name='home'),
]
