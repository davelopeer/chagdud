from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'khadro_ling/home.html'


class AboutUsView(TemplateView):
    template_name = 'khadro_ling/about_us.html'
