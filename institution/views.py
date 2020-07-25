from django.views.generic import TemplateView


class HomeView(TemplateView):
     template_name = 'institution/home.html'


class AboutUsView(TemplateView):
    template_name = 'institution/about_us.html'
