from django.db import models
from django.db.models.base import Model
from tinymce.models import HTMLField
from datetime import date


MONTHS = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro',
]

class CieloLinks(models.Model):
  title = models.CharField(max_length=500)
  url = models.URLField()

  class Meta:
      verbose_name = 'Link Cielo'
      verbose_name_plural = 'Links Cielo'

  def __str__(self):
      return self.title

class FutureEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            start_date__gte=date.today()).order_by('start_date')

class Event(models.Model):
    EVENT_TYPE_OPTIONS = (
        ('online', 'On-line'),
        ('presential', 'Presencial'),
    )

    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_OPTIONS)

    name_pt = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500)
    name_es = models.CharField(max_length=500)

    vajra_master = models.CharField(max_length=200)

    requirements_pt = models.CharField(max_length=1000, null=True, blank=True)
    requirements_en = models.CharField(max_length=1000, null=True, blank=True)
    requirements_es = models.CharField(max_length=1000, null=True, blank=True)

    place_pt = models.CharField(max_length=200)
    place_en = models.CharField(max_length=200)
    place_es = models.CharField(max_length=200)

    description_pt = models.TextField(max_length=20000)
    description_en = models.TextField(max_length=20000)
    description_es = models.TextField(max_length=20000)

    short_description_pt = models.TextField(max_length=1000)
    short_description_en = models.TextField(max_length=1000)
    short_description_es = models.TextField(max_length=1000)

    event_image = models.ImageField()

    participation_text_pt = HTMLField()
    participation_text_en = HTMLField()
    participation_text_es = HTMLField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    cielo_link = models.ManyToManyField(CieloLinks)
    paypal_link = models.URLField()

    # Accommodations
    amitaba_accommodation_capacity = models.PositiveIntegerField(verbose_name="Lotação Amitaba", null=True, blank=True)
    amitaba_accommodation_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço Amitaba", null=True, blank=True)

    retreat_house_accommodation_capacity = models.PositiveIntegerField(verbose_name="Lotação casa de retiro", null=True, blank=True)
    retreat_house_accommodation_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço casa de retiro", null=True, blank=True)

    dormitory_accommodation_capacity = models.PositiveIntegerField(verbose_name="Lotação dormitório", null=True, blank=True)
    dormitory_accommodation_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço dormitório", null=True, blank=True)

    no_accommodation_capacity = models.PositiveIntegerField(verbose_name="Lotação sem acomodação", null=True, blank=True)
    no_accommodation_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço sem acomodação", null=True, blank=True)

    online_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço do evento on-line", null=True, blank=True)

    policies_pt = HTMLField()
    policies_en = HTMLField()
    policies_es = HTMLField()

    objects = models.Manager()
    events_to_come = FutureEventManager()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'{self.name_pt}  |  {self.month_verbose_name(self.start_date.month)}/{self.start_date.year}'
  
    def get_name(self, lang='pt'):
      return getattr(self, 'name_' + lang)

    def get_requirements(self, lang='pt'):
      return getattr(self, 'requirements_' + lang)

    def get_place(self, lang='pt'):
      return getattr(self, 'place_' + lang)

    def get_description(self, lang='pt'):
      return getattr(self, 'description_' + lang)

    def get_short_description(self, lang='pt'):
      return getattr(self, 'short_description_' + lang)

    def get_participation_text(self, lang='pt'):
      return getattr(self, 'participation_text_' + lang)

    def get_policies(self, lang='pt'):
      return getattr(self, 'policies_' + lang)

    @property
    def start_date_pretty(self):
        if self.start_date.year == self.end_date.year:
            if self.start_date.month == self.end_date.month:
                return f'{self.start_date.day}, às {self.start_date.hour}h'
            return f'{self.start_date.day} de {self.month_verbose_name(self.start_date.month)},' \
                   f' às {self.start_date.hour}h'
        return f'{self.start_date.day} de {self.month_verbose_name(self.start_date.month)}' \
               f' de {self.start_date.year}, às {self.start_date.hour}h'

    @property
    def end_date_pretty(self):
        return f'{self.end_date.day} de {self.month_verbose_name(self.end_date.month)}' \
               f' de {self.end_date.year}, às {self.end_date.hour}h'

    @property
    def short_month(self):
        """
        Small representation of the month with 3 initial letters.

        Return
        Month initials (e.g.: jan)
        """
        return self.month_verbose_name(self.start_date.month)[:3]

    def month_verbose_name(self, month):
        """
        Month verbose name.

        Args
        month (int): index for month in const variable

        Return (str)
        Month verbose name
        """
        return MONTHS[month - 1]
