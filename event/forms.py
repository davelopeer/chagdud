from django import forms
from django.conf import settings
from django.core.mail import EmailMessage

class EventForm(forms.Form):
    PAYMENT_CHOICES = (
        ('deposito', 'Depósito Bancário'),
        ('credito', 'Cartão de Crédito'),
    )

    STATES_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('Pi', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'nome',
        'name': 'nome'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'id': 'email',
        'name': 'email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'telefone',
        'name': 'telefone'
    }))
    birth_date = forms.DateField(widget=forms.TextInput(attrs={
        'type': 'date',
        'class': 'form-control',
        'id': 'dataNascimento',
        'name': 'dataNascimento',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'endereco',
        'name': 'endereco',
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'cidade',
        'name': 'cidade',
    }))
    state = forms.ChoiceField(choices=STATES_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'Estado',
        'name': 'estado',
    }))

    cep = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'CEP',
        'name': 'CEP',
    }))

    accepts_policy_terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'type': 'checkbox',
        'class': 'form-check-input',
        'value': 'aceito',
        'id': 'aceitoPolitica',
    }))

    payment_options = forms.ChoiceField(required=False, choices=PAYMENT_CHOICES, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'evento'
    }))

    deposit_date = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type':'date',
        'class':'form-control',
        'id':'data',
        'name':'data'
    }))

    deposit_value = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'valor', 
        'name':'valor',
        'step': '.05',
        'min': '0'
    }))

    deposit_receipt = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'type': 'file',
        'class': 'form-control-file',
        'name': 'comprovante',
        'id': 'comprovante'
    }))

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        birth_date = self.cleaned_data['birth_date']
        address = self.cleaned_data['address']
        city = self.cleaned_data['city']
        state = self.cleaned_data['state']
        cep = self.cleaned_data['cep']
        deposit_date = self.cleaned_data['deposit_date'] if self.cleaned_data['deposit_date'] else '-'
        deposit_value = self.cleaned_data['deposit_value'] if self.cleaned_data['deposit_value'] else '-'


        subject = f'Inscrição de {name}'
        message = f'''
            name: {name}
            email: {email}
            phone: {phone}
            birth_date: {birth_date}
            address: {address}
            city: {city}
            state: {state}
            cep: {cep}
            deposit_date: {deposit_date}
            deposit_value: {deposit_value}
        '''

        mail = EmailMessage(
            subject,
            message,
            settings.CONTACT_EMAIL,
            [settings.CONTACT_EMAIL]
        )

        if self.cleaned_data['deposit_receipt']:
            deposit_receipt = self.cleaned_data['deposit_receipt']
            mail.attach(deposit_receipt.name, deposit_receipt.read())

        return mail.send()

class PresentialEventForm(EventForm):
    GENDER_CHOICES = (
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('other', 'Outro'),
    )
    FOOD_PREFERENCE_CHOICES = (
        ('vegetarian', 'Vegetariano'),
        ('non-vegetarian', 'Não-Vegetariano'),
    )
    NEEDS_CHAIR_CHOICES = (
        ('yes', 'Sim'),
        ('no', 'Não'),
    )
    ACCOMMODATION_OPTION_CHOICES = (
        ('amitaba', 'Alimentação e hospedagem no Amitaba'),
        ('retreat', 'Alimentação e hospedagem na casa de retiro'),
        ('dormitory', 'Alimentação e hospedagem no dormitório'),
        ('no-accommodation', 'Alimentação e sem hospedagem'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'genero'
    }))
    food_preference = forms.ChoiceField(choices=FOOD_PREFERENCE_CHOICES, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'alimentar'
    }))
    needs_chair = forms.ChoiceField(choices=NEEDS_CHAIR_CHOICES, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'cadeira'
    }))

    arrive_date = forms.DateTimeField(widget=forms.TextInput(attrs={
        'type': 'datetime-local',
        'class': 'form-control',
        'id': 'dataChegada',
        'name': 'dataChegada',
    }))
    depart_date = forms.DateTimeField(widget=forms.TextInput(attrs={
        'type': 'datetime-local',
        'class': 'form-control',
        'id': 'dataPartida',
        'name': 'dataPartida',
    }))
    observations = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'observacoes',
        'name': 'observacoes',
        'rows': '3',
    }))

    accommodation_option = forms.ChoiceField(choices=ACCOMMODATION_OPTION_CHOICES, widget=forms.RadioSelect(attrs={
        'class':'form-check-input',
        'type':'radio',
        'name':'evento'
    }))

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        birth_date = self.cleaned_data['birth_date']
        address = self.cleaned_data['address']
        city = self.cleaned_data['city']
        state = self.cleaned_data['state']
        cep = self.cleaned_data['cep']
        gender = self.cleaned_data['gender']
        food_preference = self.cleaned_data['food_preference']
        needs_chair = self.cleaned_data['needs_chair']
        arrive_date = self.cleaned_data['arrive_date']
        depart_date = self.cleaned_data['depart_date']
        observations = self.cleaned_data['observations']
        accommodation_option = self.cleaned_data['accommodation_option']
        accepts_policy_terms = self.cleaned_data['accepts_policy_terms']
        deposit_date = self.cleaned_data['deposit_date'] if self.cleaned_data['deposit_date'] else '-'
        deposit_value = self.cleaned_data['deposit_value'] if self.cleaned_data['deposit_value'] else '-'

        subject = f'Inscrição de {name}'
        message = f'''
            name: {name}
            email: {email}
            phone: {phone}
            birth_date: {birth_date}
            address: {address}
            city: {city}
            state: {state}
            cep: {cep}
            gender: {gender}
            food_preference: {food_preference}
            needs_chair: {needs_chair}
            arrive_date: {arrive_date}
            depart_date: {depart_date}
            observations: {observations}
            accommodation_option: {accommodation_option}
            accepts_policy_terms: {accepts_policy_terms}
            deposit_date: {deposit_date}
            deposit_value: {deposit_value}
        '''

        mail = EmailMessage(
            subject,
            message,
            settings.CONTACT_EMAIL,
            [settings.CONTACT_EMAIL]
        )

        if self.cleaned_data['deposit_receipt']:
            deposit_receipt = self.cleaned_data['deposit_receipt']
            mail.attach(deposit_receipt.name, deposit_receipt.read())

        return mail.send()
