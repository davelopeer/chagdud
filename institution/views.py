from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse

from institution.forms import ContactForm
from institution.models import News


class HomeView(TemplateView):
     template_name = 'institution/home.html'

     def get_context_data(self, **kwargs):
          context = super(HomeView, self).get_context_data(**kwargs)
          context['news_list_1'] = News.objects.all()[0:3]
          context['news_list_2'] = News.objects.all()[3:6]
          return context


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


class NewsListView(ListView):
     model = News
     context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
