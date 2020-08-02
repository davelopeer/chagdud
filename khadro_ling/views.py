from django.views.generic import View, TemplateView, ListView, DetailView
from khadro_ling.models import Event


class HomeView(TemplateView):
    template_name = 'khadro_ling/home.html'


class AboutUsView(TemplateView):
    template_name = 'khadro_ling/about_us.html'


class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class OfferingsView(TemplateView):
    template_name = 'khadro_ling/offerings.html'
