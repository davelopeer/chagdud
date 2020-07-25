from django.urls import path
from institution.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
