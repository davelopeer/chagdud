from django import forms
from django.core.mail import EmailMessage

class EventForm(forms.Form):
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
        ('amitaba', 'Alimentação e hospedagem no Amitaba:R$ 414,00'),
        ('retreat', 'Alimentação e hospedagem na casa de retiro: R$ 394,00'),
        ('dormitory', 'Alimentação e hospedagem no dormitório: R$ 340,00'),
        ('no-accommodation', 'Alimentação e sem hospedagem: R$ 296,00'),
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
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'type': 'number',
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
    state = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
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

    accepts_policy_terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'type': 'checkbox',
        'class': 'form-check-input',
        'value': 'aceito',
        'id': 'aceitoPolitica',
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
        '''

        mail = EmailMessage(
            subject,
            message,
            settings.CONTACT_EMAIL,
            [settings.CONTACT_EMAIL]
        )
        print('-'*20)
        print('Enviado')
        print('-'*20)
        return mail.send()