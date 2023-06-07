from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('region/<str:region>/', views.region, name='region'),
    path('region/<str:region>/<str:country>/', views.country, name='country'),
]