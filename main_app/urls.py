from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('region/<str:region>/', views.region, name='region'),
    path('region/<str:region>/<str:country>/', views.country, name='country'),
    path('region/<str:region>/<str:country>/visit/<int:country_id>', views.country_visit, name='country_visit'),
    path('region/<str:region>/<str:country>/wishlist/<int:country_id>', views.country_wishlist, name='country_wishlist'),
    path('profile/visited/', views.visited, name='visited'),
    path('profile/wishlist/', views.wishlist, name='wishlist'),
]