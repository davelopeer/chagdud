from django.views.generic import TemplateView


class KhadroLingHomeView(TemplateView):
    template_name = 'khadro_ling/home.html'

class KhadroLingAboutUsView(TemplateView):
    template_name = 'khadro_ling/about_us.html'