from django.urls import path
from institution.views import HomeView, AboutUsView, TeachersView, \
    DownloadsView

app_name = 'institution'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('downloads/', DownloadsView.as_view(), name='downloads'),
    path('professores/', TeachersView.as_view(), name='teachers'),
    path('quem-somos/', AboutUsView.as_view(), name='about-us'),
]
