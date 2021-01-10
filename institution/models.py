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
