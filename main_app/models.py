from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Country(models.Model):
    official_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    subregion = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    independent = models.BooleanField()
    population = models.IntegerField()
    area = models.FloatField()
    google_maps = models.URLField()
    currencies = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    flag_png = models.URLField()
    flag_alt = models.TextField()


    def __str__(self):
        return self.name