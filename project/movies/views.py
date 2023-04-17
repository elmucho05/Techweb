from django.shortcuts import render
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import Film
from django.contrib.auth import logout, authenticate, login

def home(request):
  films = Film.objects.all().order_by("genre_id")
  genres = films.values("genre_id").distinct()
  context = {
    "genres" : genres,
    "films" : films,
  }
  return render(request, "movies/home.html", context) 

def browse(request):
  genre  = request.GET.get("genre", None)
  search = request.GET.get("search", None)

  films = []

  if genre:
    films = Film.objects.filter(genre=genre)
  elif search:
    films = Film.objects.filter(name__icontains=search)
    messages.info(request, mark_safe(f'{len(films)} risultati per <b>{search}</b>'))

  context = {
    "genre" : genre,
    "search" : search,
    "films" : films,
  }
  return render(request, "movies/browse.html", context) 

def details(request, film_id):
  film = Film.objects.get(id=film_id)
  context = {
    "film" : film 
  }
  return render(request, "movies/details.html", context) 

