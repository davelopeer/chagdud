from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from tinymce.models import HTMLField



class Offering(object):

  @staticmethod
  def send_user_confirmation_email(data):
    context = {
      'name': data['name']
    }
    email = data['email']

    subject = f'Oferenda enviada com sucesso'
    message = render_to_string('offering/email/email_user_confirmation.html', context)

    mail = EmailMessage(
        subject,
        message,
        settings.CONTACT_EMAIL,
        [email]
    )
    mail.content_subtype = "html"

    return mail.send()

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
        'lamps': data['lamps'],
        'prayer_flags': data['prayer_flags'],
        'dedication': data['dedication'],
        'deposit_date': data['deposit_date'],
        'deposit_value': data['deposit_value'],
    }

    subject = f'Oferenda'
    message = render_to_string('offering/email/email_data.html', context)

    mail = EmailMessage(
        subject,
        message,
        settings.CONTACT_EMAIL,
        [settings.CONTACT_EMAIL]
    )
    mail.content_subtype = "html"

    if data['deposit_receipt']:
      deposit_receipt = data['deposit_receipt']
      mail.attach(deposit_receipt.name, deposit_receipt.read())

    return mail.send()


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

    mail = EmailMessage(
        subject,
        message,
        settings.CONTACT_EMAIL,
        [settings.CONTACT_EMAIL]
    )
    mail.content_subtype = "html"

    if data['deposit_receipt']:
      deposit_receipt = data['deposit_receipt']
      mail.attach(deposit_receipt.name, deposit_receipt.read())

    return mail.send()