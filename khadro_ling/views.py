from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.shortcuts import render

from khadro_ling.models import Event
from khadro_ling.forms import EventForm


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

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['form'] = EventForm
        return context


class EventDetailFormView(FormView):
    form_class = EventForm
    success_url = '/khadroling/evento/'
    template_name = 'khadro_ling/about_us.html'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    # REMOVE AFTER APPROVED
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

