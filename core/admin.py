from django.contrib import admin
from .models import User, Profile, Medical, Ment

model_list = [User, Profile, Medical, Ment]
admin.site.register(model_list)
