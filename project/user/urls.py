from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/user/<uid>/profile/
  path('profile/', views.view_profile, name="view_profile"),

  # http://127.0.0.1:8000/user/<uid>/set-avatar
  path('update-avatar/', views.view_update_user_avatar, name="view_update_user_avatar"),
]