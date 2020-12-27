from django.shortcuts import render
from offering.forms import OfferingForm


def offerings_view(request):
    template = 'offering/offerings.html'
    context = {
       'form': OfferingForm()
    }

    if request.method == 'POST':
        post_keys = request.POST.keys()
        if 'general-form' in post_keys:
            form = OfferingForm(request.POST, request.FILES)

        if form.is_valid():
            mail_sended = form.send_email()
            context['mail_sended'] = True if mail_sended else False

    return render(request, template, context=context)
