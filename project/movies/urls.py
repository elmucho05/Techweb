from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/home
  path('', lambda request: redirect('home/', permanent=True)),
  path('home/', views.home, name="home"),

  # http://127.0.0.1:8000/browse/
  path('browse/', views.browse, name="browse"),

  path('film/<int:film_id>', views.details, name="details"),
]