from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Country, Profile, Comment
from .forms import CommentForm

REGIONS = ['Asia', 'Oceania', 'Europe', 'Americas', 'Antarctic', 'Africa']

def home(request):
  return render(request, 'home.html', {'regions': REGIONS})

def region(request, region):
  profile = Profile.objects.get(user=request.user)
  wishlist = profile.wishlist.all()
  visited = profile.visited.all()
  countries = Country.objects.filter(region=region).order_by('common_name')
  return render(request, 'countries/regions.html', {
        'countries': countries, 'wishlist': wishlist, 'visited': visited })

def country(request, region, country):
  country = Country.objects.get(common_name=country)
  comments = Comment.objects.filter(country=country.id)
  comment_form = CommentForm()
  return render(request, 'countries/country.html', {
        'country': country, 'comment_form': comment_form, 'comments': comments })

def visited(request):
  profile = Profile.objects.get(user=request.user)
  countries = profile.visited.all()
  wishlist = profile.wishlist.all()
  return render(request, 'profile/visited.html', {
        'countries': countries, 'wishlist': wishlist })

def wishlist(request):
  profile = Profile.objects.get(user=request.user)
  countries = profile.wishlist.all()
  visited = profile.visited.all()
  return render(request, 'profile/wishlist.html', {
        'countries': countries, 'visited': visited })

def visit_wishlist_redirect(request, region):
  referer = request.META.get('HTTP_REFERER')
  if 'wishlist' in referer:
    return redirect('wishlist')
  elif 'visited' in referer:
    return redirect('visited')
  else:
    return redirect('region', region)

def country_visit(request, region, country, country_id):
  Profile.objects.get(user=request.user).visited.add(country_id)
  return visit_wishlist_redirect(request, region)

def country_wishlist(request, region, country, country_id):
  Profile.objects.get(user=request.user).wishlist.add(country_id)
  return visit_wishlist_redirect(request, region)

def country_visit_remove(request, region, country, country_id):
  Profile.objects.get(user=request.user).visited.remove(country_id)
  return visit_wishlist_redirect(request, region)

def country_wishlist_remove(request, region, country, country_id):
  Profile.objects.get(user=request.user).wishlist.remove(country_id)
  return visit_wishlist_redirect(request, region)

def country_comment(request, region, country):
  form = CommentForm(request.POST)
  country_obj = Country.objects.get(common_name=country)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.country = country_obj
    new_comment.user = request.user
    new_comment.save()
  return redirect('country', country_obj.region, country)

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