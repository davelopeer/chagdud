from django.db import models


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

class Event(models.Model):
    name = models.CharField(max_length=500)
    vajra_master = models.CharField(max_length=200)
    requirements = models.CharField(max_length=1000, null=True, blank=True)
    place = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    short_description = models.TextField(max_length=1000)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.id) + self.name

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


class Offering(models.Model):
    name = models.CharField(max_length=500)