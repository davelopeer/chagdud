from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

from event.models import Event
from event.forms import EventForm, PresentialEventForm


class EventListView(ListView):
    template_name = 'event/event_list.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.events_to_come.all()

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)

        if 'django_language' in self.request.COOKIES.keys():
          context['user_language'] = self.request.COOKIES['django_language']
        else:
          context['user_language'] = 'pt'

        return context

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        # ------------------------------
        # Different forms for online and presential events
        context = super(EventDetailView, self).get_context_data(**kwargs)

        event_id = self.kwargs['pk']
        event = self.get_queryset().get(pk=event_id)

        if 'django_language' in self.request.COOKIES.keys():
          context['user_language'] = self.request.COOKIES['django_language']
        else:
          context['user_language'] = 'pt'

        if event.event_type == 'online':
            context['form'] = EventForm
        elif event.event_type == 'presential':
            context['form'] = PresentialEventForm

        return context

    def get_template_names(self, **kwargs):
        # ------------------------------
        # Different templates for online and presential events
        event_id = self.kwargs['pk']
        event = self.get_queryset().get(pk=event_id)
        if event.event_type == 'online':
            return 'event/event_online_detail.html'
        elif event.event_type == 'presential':
            return 'event/event_presential_detail.html'

class OnlineEventFormView(FormView):
    form_class = EventForm
    success_url = '/khadroling/evento/'

    def form_valid(self, form):
      form.send_email()
      return super().form_valid(form)

class PresentialEventFormView(FormView):
    form_class = PresentialEventForm
    success_url = '/khadroling/evento/'

    def form_valid(self, form):
      form.send_email()
      return super().form_valid(form)
