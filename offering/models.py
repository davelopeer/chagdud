from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


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
        'offering_value': data['offering_value'],
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

    deposit_receipt = data['deposit_receipt']
    mail.attach(deposit_receipt.name, deposit_receipt.read())

    return mail.send()