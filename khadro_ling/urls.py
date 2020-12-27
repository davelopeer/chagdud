from django.urls import path
from django.views.decorators.http import require_POST
from khadro_ling.views import HomeView, AboutUsView, EventListView,  \
    EventDetailView, EventDetailFormView

from offering.views import offerings_view

app_name = 'khadroling'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('evento/', EventListView.as_view(), name='event-list'),
    path('evento/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('evento-form/', require_POST(EventDetailFormView.as_view()), name='event-form'),
    path('oferendas/', offerings_view, name='offerings'),
    path('quem-somos/', AboutUsView.as_view(), name='about-us'),
]
