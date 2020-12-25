from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.shortcuts import render

from khadro_ling.models import Event
from khadro_ling.forms import TsogForm, LampForm, RiwoSangchodForm, FlagForm, AkshobiaForm, \
    CerimonialForm, DonationForm, EventForm


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

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['form'] = EventForm
        return context


class EventDetailFormView(FormView):
    form_class = EventForm
    success_url = '/khadroling/evento/'
    template_name = 'khadro_ling/about_us.html'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    # REMOVE AFTER APPROVED
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


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
            form = TsogForm(request.POST, request.FILES)
        elif 'lamp' in post_keys:
            form = LampForm(request.POST, request.FILES)
        elif 'riwo_sangchod' in post_keys:
            form = RiwoSangchodForm(request.POST, request.FILES)
        elif 'flag' in post_keys:
            form = FlagForm(request.POST, request.FILES)
        elif 'akshobia' in post_keys:
            form = AkshobiaForm(request.POST, request.FILES)
        elif 'cerimonial' in post_keys:
            form = CerimonialForm(request.POST, request.FILES)
        elif 'donation' in post_keys:
            form = DonationForm(request.POST, request.FILES)

        if form.is_valid():
            mail_sended = form.send_email()
            context['mail_sended'] = True if mail_sended else False

    return render(request, template, context=context)
