from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/
  path('home/', views.home, name="home"),

  # http://127.0.0.1:8000/titles/<id>
  path('titles/<id>', views.view_details, name="view_details"),

  # http://127.0.0.1:8000/watch/<id>
  path('watch/<id>', views.view_watch, name="view_watch"),

  # http://127.0.0.1:8000/films?genre=<genre>
  path('films/', views.view_films, name="view_films"),

  # http://127.0.0.1:8000/tv-serie?genre=<genre>
  path('tv-series/', views.view_series, name="view_series"),

  # http://127.0.0.1:8000/browse?genre=<genre>
  # http://127.0.0.1:8000/browse?search=<search>
  path('browse/', views.view_browse, name="view_browse"),
]