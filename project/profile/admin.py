from django.contrib import admin
from .models import UserProfile, UserComment, SubscriptionType, UserSubscription

admin.site.register(UserProfile)
admin.site.register(UserComment)
admin.site.register(SubscriptionType)
admin.site.register(UserSubscription)
