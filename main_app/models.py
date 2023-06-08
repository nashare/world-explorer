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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visited = models.ManyToManyField('Country', related_name='visitors')
    wishlist = models.ManyToManyField('Country', related_name='wishlisted')

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.CASCADE)