from django.contrib import admin
from .models import UserProfile, UserComment, SubscriptionType, UserSubscription, UserPurchase

admin.site.register(UserProfile)
admin.site.register(UserComment)
admin.site.register(SubscriptionType)
admin.site.register(UserSubscription)
admin.site.register(UserPurchase)