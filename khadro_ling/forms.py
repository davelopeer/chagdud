from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


PAYMENT_TYPES = (
    ('transferencia', 'Transferência entre contas Banco do Brasil'),
    ('doc/ted', 'DOC ou TED'),
    ('deposito', 'Depósito')
)

OFFERING_PERIOD = (
    ('1 por dia', '1 por dia'),
    ('mais de uma por dia', 'Mais de uma por dia'),
    ('todas no mesmo dia', 'Todas no mesmo dia')
)

class BaseOfferingForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type':'text',
        'class':'form-control',
        'id':'nome',
        'name':'nome'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type':'email',
        'class':'form-control',
        'id':'email',
        'name':'email'
    }))

    offering_value = forms.DecimalField(min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'valor', 
        'name':'valor',
        'step': '.01',
        'min': '0'
    }))

    dedication = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'observacoes',
        'name':'dedicacao',
        'rows':'3',
        'placeholder':'Nome da pessoa ou sua intenção ao oferecer'
    }))

    deposit_date = forms.CharField(widget=forms.TextInput(attrs={
        'type':'date',
        'class':'form-control',
        'id':'data',
        'name':'data'
    }))

    payment_type = forms.ChoiceField(choices=PAYMENT_TYPES, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'pagamento'
    }))

    deposit_receipt = forms.FileField(widget=forms.FileInput(attrs={
        'type': 'file',
        'class': 'form-control-file',
        'name': 'comprovante',
        'id': 'comprovante'
    }))

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        offering_value = self.cleaned_data['offering_value']
        dedication = self.cleaned_data['dedication']
        deposit_date = self.cleaned_data['deposit_date']
        payment_type = self.cleaned_data['payment_type']
        deposit_receipt = self.cleaned_data['deposit_receipt']

        subject = f'{self.verbose_offerend_type} de {name}',
        message = f'''
            Valor: {offering_value}\n
            Dedicação: {dedication}\n
            Data de depósito: {deposit_date}\n
            Tipo de pagamento: {payment_type}\n
            '''

        mail = EmailMessage(
            subject,
            message,
            settings.CONTACT_EMAIL,
            [settings.CONTACT_EMAIL]
        )
        mail.attach(deposit_receipt.name, deposit_receipt.read())
        return mail.send()

    @property
    def verbose_offerend_type(self):
        return "Oferenda"


class TsogForm(BaseOfferingForm):
    
    @property
    def verbose_offerend_type(self):
        return "Oferenda de Tsog"


class LampForm(BaseOfferingForm):
    number_of_lamps = forms.IntegerField(min_value=1, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'qtdLamparinas',
        'name':'qtdLamparinas'
    }))
    offering_period = forms.ChoiceField(choices=OFFERING_PERIOD, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'oferLamparina'
    }))

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        offering_value = self.cleaned_data['offering_value']
        dedication = self.cleaned_data['dedication']
        deposit_date = self.cleaned_data['deposit_date']
        payment_type = self.cleaned_data['payment_type']
        number_of_lamps = self.cleaned_data['number_of_lamps']
        offering_period = self.cleaned_data['offering_period']

        message = f'''
            Valor: {offering_value}\n
            Número de lamparinas: {number_of_lamps}\n
            Oferecendo: {offering_period}\n
            Dedicação: {dedication}\n
            Data de depósito: {deposit_date}\n
            Tipo de pagamento: {payment_type}\n
            '''

    @property
    def verbose_offerend_type(self):
        return "Oferenda de Lamparinas"


class RiwoSangchodForm(BaseOfferingForm):

    @property
    def verbose_offerend_type(self):
        return "Oferenda de Riwo Sangchod"

class FlagForm(BaseOfferingForm):

    @property
    def verbose_offerend_type(self):
        return "Oferenda de Bandeiras de Oração"


class AkshobiaForm(BaseOfferingForm):

    @property
    def verbose_offerend_type(self):
        return "Oferenda de Akshobia"


class CerimonialForm(BaseOfferingForm):

    @property
    def verbose_offerend_type(self):
        return "Oferenda Cerimoniais"


class DonationForm(BaseOfferingForm):

    @property
    def verbose_offerend_type(self):
        return "Doação"
