from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Country(models.Model):
    official_name = models.CharField(max_length=1000)
    common_name = models.CharField(max_length=1000)
    region = models.CharField(max_length=1000)
    subregion = models.CharField(max_length=1000)
    capital = models.CharField(max_length=1000)
    independent = models.CharField(max_length=1000)
    population = models.IntegerField()
    area = models.FloatField()
    google_maps = models.URLField()
    currencies = models.CharField(max_length=1000)
    languages = models.CharField(max_length=1000)
    flag_png = models.URLField()
    flag_alt = models.TextField()


    def __str__(self):
        return self.common_name