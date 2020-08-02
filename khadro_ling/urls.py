from django.urls import path
from khadro_ling.views import HomeView, AboutUsView, EventListView,  \
    EventDetailView, OfferingsView


app_name = 'khadroling'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('evento/', EventListView.as_view(), name='event-list'),
    path('evento/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('oferendas/', OfferingsView.as_view(), name='offerings'),
    path('quem-somos/', AboutUsView.as_view(), name='about-us'),
]
