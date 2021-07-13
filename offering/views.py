from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse

from offering.forms import OfferingForm, DrubchenOfferingForm
from offering.models import DrubchenOffering


def offerings_view(request):
    template = 'offering/offerings.html'
    context = {
       'form': OfferingForm()
    }

    if 'django_language' in request.COOKIES.keys():
      context['user_language'] = request.COOKIES['django_language']
    else:
      context['user_language'] = 'pt'

    if request.method == 'POST':
        post_keys = request.POST.keys()
        if 'general-form' in post_keys:
          form = OfferingForm(request.POST, request.FILES)

          if form.is_valid():
            mail_sended = form.send_email()
            context['mail_sended'] = True if mail_sended else False
          else:
            print(form.errors)

    return render(request, template, context=context)


class DrubchenOfferingDetailView(DetailView):
    model = DrubchenOffering
    context_object_name = 'offering'

    def get_context_data(self, **kwargs):
        context = super(DrubchenOfferingDetailView, self).get_context_data(**kwargs)

        context['user_language'] = 'pt-br'
        context['form'] = DrubchenOfferingForm

        return context

class DrubchenOfferingFormView(FormView):
    form_class = DrubchenOfferingForm
    success_url = '/khadroling/oferendas/'
    template_name = 'khadro_ling/about_us.html'

    def form_valid(self, form):
        # form.send_email()
        # import pdb; pdb.set_trace()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('offering:', kwargs={'app_label': 'auth'})