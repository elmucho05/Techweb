from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/authentication/login
  path("login/", views.view_login, name="view_login"),

  # http://127.0.0.1:8000/authentication/signup
  path("signup/", views.view_signup, name="view_signup"),

  # http://127.0.0.1:8000/authentication/signup
  path("logout/", views.logout, name="logout"),
]