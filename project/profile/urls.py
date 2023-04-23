from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/u/<uid>/profile/
  path('profile/', views.ViewProfile.as_view(), name="view_profile"),

  # http://127.0.0.1:8000/u/<uid>/update-avatar
  path('update-avatar/', views.view_update_user_avatar, name="view_update_user_avatar"),

  # http://127.0.0.1:8000/u/<uid>/update-password
  path('update-password/', views.view_update_user_password, name="view_update_user_password"),
]