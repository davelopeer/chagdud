from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from tinymce.models import HTMLField
from institution.helpers import send_mail



class Offering(object):

  @staticmethod
  def send_user_confirmation_email(data):
    context = {
      'name': data['name']
    }
    email = data['email']

    subject = f'Oferenda enviada com sucesso'
    message = render_to_string('offering/email/email_user_confirmation.html', context)

    return send_mail(
      to=email,
      subject=subject,
      body=message
    )

  @staticmethod
  def send_offering_data_email(data):
    context = {
        'name': data['name'],
        'email': data['email'],
        'crescent_moon_tara_tsog': data['crescent_moon_tara_tsog'],
        'guru_tsog': data['guru_tsog'],
        'waning_moon_tara_tsog': data['waning_moon_tara_tsog'],
        'dakini_tsog': data['dakini_tsog'],
        'riwo_sangcho': data['riwo_sangcho'],
        'general_temple_activities': data['general_temple_activities'],
        'lamps_quantity': data['lamps_quantity'],
        'lamps_quantity_by_day': data['lamps_quantity_by_day'],
        'prayer_flags': data['prayer_flags'],
        'dedication': data['dedication'],
        'deposit_date': data['deposit_date'],
        'deposit_value': data['deposit_value'],
    }

    email = data['email']
    subject = f'Oferenda'
    message = render_to_string('offering/email/email_data.html', context)

    if data['deposit_receipt']:
      deposit_receipt = data['deposit_receipt']
    else:
      deposit_receipt = None

    return send_mail(
      to=email,
      subject=subject,
      body=message,
      attachment=deposit_receipt
    )

class DrubchenOffering(models.Model, Offering):
  slug = models.SlugField()
  title = models.CharField(max_length=500)
  text = HTMLField()

  class Meta:
    verbose_name = 'Oferenda de Drubchen'
    verbose_name_plural = 'Oferendas de Drubchen'
    ordering = ['-id']

  def __str__(self):
    return f'{self.title}'

  @staticmethod
  def send_offering_data_email(data):
    context = {
        'name': data['name'],
        'email': data['email'],
        'offering_value': data['offering_value'],
        'value_for_tsogs': data['value_for_tsogs'],
        'value_for_substances': data['value_for_substances'],
        'value_for_lamps': data['value_for_lamps'],
        'dedication': data['dedication'],
        'deposit_date': data['deposit_date'],
        'observations': data['observations'],
    }

    subject = f'Oferenda de Drubchen'
    message = render_to_string('offering/email/drubchen_email_data.html', context)

    if data['deposit_receipt']:
      deposit_receipt = data['deposit_receipt']
    else:
      deposit_receipt = None

    return send_mail(
      to=email,
      subject=subject,
      body=message,
      attachment=deposit_receipt
    )