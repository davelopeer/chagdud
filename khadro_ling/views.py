from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import render

from khadro_ling.models import Event
from khadro_ling.forms import TsogForm, LampForm, RiwoSangchodForm, FlagForm, AkshobiaForm, \
    CerimonialForm, DonationForm


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


def offerings_view(request):
    template = 'khadro_ling/offerings.html'
    context = {
       'tsog_form': TsogForm(),
       'lamp_form': LampForm(),
       'riwo_sangchod_form': RiwoSangchodForm(),
       'flag_form': FlagForm(),
       'akshobia_form': AkshobiaForm(),
       'cerimonial_form': CerimonialForm(),
       'donation_form': DonationForm(),
    }

    if request.method == 'POST':
        post_keys = request.POST.keys()
        if 'tsog' in post_keys:
            form = TsogForm(request.POST)
        elif 'lamp' in post_keys:
            form = LampForm(request.POST)
        elif 'riwo_sangchod' in post_keys:
            form = RiwoSangchodForm(request.POST)
        elif 'flag' in post_keys:
            form = FlagForm(request.POST)
        elif 'akshobia' in post_keys:
            form = AkshobiaForm(request.POST)
        elif 'cerimonial' in post_keys:
            form = CerimonialForm(request.POST)
        elif 'donation' in post_keys:
            form = DonationForm(request.POST)

        if form.is_valid():
            mail_sended = form.send_email()
            context['mail_sended'] = True if mail_sended else False

    return render(request, template, context=context)
