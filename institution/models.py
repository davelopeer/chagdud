from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class News(models.Model):
  title = models.CharField(max_length=500)
  image = models.ImageField(null=True, blank=True)
  text = HTMLField()

  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'Novidade'
    verbose_name_plural = 'Novidades'
    ordering = ['-id']

  def __str__(self):
    return f'{self.title}'


class SacredDates(models.Model):
  title = models.CharField(max_length=1000)
  text = HTMLField()

  class Meta:
    verbose_name = 'Datas Sagradas'
    verbose_name_plural = 'Datas Sagradas'

  def __str__(self):
    return f'{self.title}'


class GenericPage(models.Model):
  slug = models.SlugField()
  title = models.CharField(max_length=500)
  image = models.ImageField(null=True, blank=True)
  text = HTMLField()

  class Meta:
    verbose_name = 'Página Genérica'
    verbose_name_plural = 'Páginas Genéricas'
    ordering = ['-id']

  def __str__(self):
    return f'{self.title}'
