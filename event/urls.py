from django.urls import path
from django.views.decorators.http import require_POST
from event.views import EventListView, EventDetailView, OnlineEventFormView, PresentialEventFormView


app_name = 'event'

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('online-form/', require_POST(OnlineEventFormView.as_view()), name='online-event-form'),
    path('presencial-form/', require_POST(PresentialEventFormView.as_view()), name='presential-event-form'),
]



