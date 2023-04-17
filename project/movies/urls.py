from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/
  path('home/', ),

  # http://127.0.0.1:8000/films
  path('films/', views.view_films, name="home"),

  # http://127.0.0.1:8000/films/<id>
  path('films/<int:title_id>', views.view_film_details, name="view_film_details"),
  
  # http://127.0.0.1:8000/films/browse?genre=<genre>
  path('films/browse', views.view_browse, name="view_browse"),




  # http://127.0.0.1:8000/tv-serie
  path('tv-series/', views.view_tvseries, name="view_tvseries"),

  # http://127.0.0.1:8000/tv-serie/browse?genre=<genre>
  path('tv-series/browse', views.view_tvseries, name="view_tvseries"),

  # http://127.0.0.1:8000/tv-serie/<id>/<season>/<episode>
  path('tv-serie/<int:title_id>', views.view_tvserie_details, name="view_tvserie_details"),
]