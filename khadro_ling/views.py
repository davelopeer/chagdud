from django.views.generic import TemplateView
from django.shortcuts import render

from event.models import Event

class HomeView(TemplateView):
    template_name = 'khadro_ling/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['events'] = Event.events_to_come.all()

        if 'django_language' in self.request.COOKIES.keys():
          context['user_language'] = self.request.COOKIES['django_language']
        else:
          context['user_language'] = 'pt'

        return context


class AboutUsView(TemplateView):
    template_name = 'khadro_ling/about_us.html'
