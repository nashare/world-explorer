from django.contrib import admin
# import your models here
from .models import Country, Profile, Comment

# Register your models here
admin.site.register(Country)
admin.site.register(Profile)
admin.site.register(Comment)