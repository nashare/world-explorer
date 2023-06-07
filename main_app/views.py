import requests
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Country, Profile

REGIONS = ['Asia', 'Oceania', 'Europe', 'Americas', 'Antarctic', 'Africa']

def home(request):
  return render(request, 'home.html', {'regions': REGIONS})

def region(request, region):
  profile = Profile.objects.get(user=request.user)
  countries = Country.objects.filter(region=region).order_by('common_name')
  return render(request, 'countries/regions.html', {
        'countries': countries, 'profile': profile })

def country(request, region, country):
  country = Country.objects.get(common_name=country)
  return render(request, 'countries/country.html', {
        'country': country })

def visited(request):
  profile = Profile.objects.get(user=request.user)
  countries = profile.visited.all()
  return render(request, 'profile/visited.html', {
        'countries': countries })

def wishlist(request):
  profile = Profile.objects.get(user=request.user)
  countries = profile.wishlist.all()
  return render(request, 'profile/wishlist.html', {
        'countries': countries })

def country_visit(request, region, country, country_id):
  Profile.objects.get(user=request.user).visited.add(country_id)
  return redirect('region', region)

def country_wishlist(request, region, country, country_id):
  Profile.objects.get(user=request.user).wishlist.add(country_id)
  return redirect('region', region)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      profile = Profile(user=user)
      profile.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up. Please try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)