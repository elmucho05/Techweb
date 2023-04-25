from django.contrib import admin
from .models import UserProfile, UserComment

admin.site.register(UserProfile)
admin.site.register(UserComment)
