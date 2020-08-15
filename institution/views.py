from django.views.generic import TemplateView


class HomeView(TemplateView):
     template_name = 'institution/home.html'


class AboutUsView(TemplateView):
    template_name = 'institution/about_us.html'


class TeachersView(TemplateView):
     template_name = 'institution/teachers.html'


class DownloadsView(TemplateView):
     template_name = 'institution/downloads.html'


class ContactView(TemplateView):
     template_name = 'institution/contact.html'


class SacredDatesView(TemplateView):
     template_name = 'institution/sacred_dates.html'