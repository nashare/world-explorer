import requests
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

REGIONS = ['Asia', 'Oceania', 'Europe', 'Americas', 'Antarctic', 'Africa']

def home(request):
  return render(request, 'home.html', {'regions': REGIONS})

def region(request, region):
  url = f'https://restcountries.com/v3.1/region/{region}'
  response = requests.get(url)
  error = ''
  if response.status_code == 200:
      countries = response.json()
  else:
      error = 'Try again'
  return render(request, 'countries/regions.html', {
        'countries': countries, 'error': error})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up. Please try again!'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)