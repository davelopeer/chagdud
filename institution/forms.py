from django import forms
from institution.helpers import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'id': 'formGroupExampleInput',
        'type': 'text'
        }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'id': 'exampleInputEmail1',
        'type': 'email',
        'aria-describedby': 'emailHelp'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'id': 'exampleFormControlTextarea1',
        'rows': 3
    }))

    def send_email(self, **kwargs):
      name = self.cleaned_data['name']
      email = self.cleaned_data['email']
      body = self.cleaned_data['message']
      
      return send_mail(
        to = email,
        subject = f'Mensagem de contato de {name}',
        body = body
      )
