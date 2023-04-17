from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/
  path('', lambda request: redirect('home')),

  # http://127.0.0.1:8000/film
  path('film/', views.view_films, name="home"),

  # http://127.0.0.1:8000/tv-serie
  path('tv-series/', views.view_tvseries, name="view_tvseries"),

  # http://127.0.0.1:8000/browse/
  path('browse/', views.view_browse, name="view_browse"),

  path('film/<int:film_id>', views.view_details, name="view_details"),
]