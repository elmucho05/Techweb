from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/authentication/login
  path("login/", views.login, name="login"),

  # http://127.0.0.1:8000/authentication/signup
  path("signup/", views.signup, name="signup"),

  # http://127.0.0.1:8000/authentication/signup
  path("logout/", views.logout, name="logout"),
]