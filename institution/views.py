from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse

from institution.forms import ContactForm


class HomeView(TemplateView):
     template_name = 'institution/home.html'


class AboutUsView(TemplateView):
    template_name = 'institution/about_us.html'


class TeachersView(TemplateView):
     template_name = 'institution/teachers.html'


class DownloadsView(TemplateView):
     template_name = 'institution/downloads.html'


class ContactView(FormView):
     template_name = 'institution/contact.html'
     form_class = ContactForm

     def form_valid(self, form):
          form.send_email()
          return super().form_valid(form)

     def get_success_url(self):
          return reverse('institution:contact')


class SacredDatesView(TemplateView):
     template_name = 'institution/sacred_dates.html'