from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=500)


class Offering(models.Model):
    name = models.CharField(max_length=500)