import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
from django.conf import settings


def send_mail(to, subject, body, attachment=None):
  message = Mail(
    from_email = settings.CONTACT_EMAIL,
    to_emails = to,
    subject = subject,
    html_content = body
  )

  if attachment:
    bytes_file = attachment.file.read()
    encoded_file = base64.b64encode(bytes_file).decode()
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(attachment.name),
        FileType(attachment.content_type),
        Disposition('attachment')
    )
    message.attachment = attachedFile

  try:
    sg = SendGridAPIClient(settings.SENDGRID_API_SECRET_KEY)
    sg.send(message)
    print('Enviou')
    return True
  except Exception as e:
    print('Falhou')
    print(e)
    return False