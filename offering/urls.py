from django.urls import path
from django.views.decorators.http import require_POST

from offering.views import offerings_view, DrubchenOfferingDetailView, DrubchenOfferingFormView


app_name = 'offering'

urlpatterns = [
    path('', offerings_view, name='offerings'),
    path('drubchen/<str:slug>/', DrubchenOfferingDetailView.as_view(), name='drubchen-offering-detail'),
    path('drubchen-offering-form/', require_POST(DrubchenOfferingFormView.as_view()), name='drubchen-offering-form'),
]



