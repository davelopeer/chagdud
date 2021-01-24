from django.views.generic import TemplateView, ListView, DetailView

from django.views.generic.edit import FormView

from event.models import Event
from event.forms import EventForm, PresentialEventForm


class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        # ------------------------------
        # Different forms for online and presential events
        context = super(EventDetailView, self).get_context_data(**kwargs)

        event = self.get_queryset().first()
        if event.event_type == 'online':
            context['form'] = EventForm
        elif event.event_type == 'presential':
            context['form'] = PresentialEventForm

        return context

    def get_template_names(self, **kwargs):
        # ------------------------------
        # Different templates for online and presential events
        event = self.get_queryset().first()

        if event.event_type == 'online':
            return 'event/event_online_detail.html'
        elif event.event_type == 'presential':
            return 'event/event_presential_detail.html'

class OnlineEventFormView(FormView):
    form_class = EventForm
    success_url = '/khadroling/evento/'
    template_name = 'khadro_ling/about_us.html'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class PresentialEventFormView(FormView):
    form_class = PresentialEventForm
    success_url = '/khadroling/evento/'
    template_name = 'khadro_ling/about_us.html'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

