from django.shortcuts import render
from .models import Genre, Film

from django.db import connection

def get_pair_genre_count_sql():
  pair = [ ]
  with connection.cursor() as cursor:
    raw = "SELECT genre_id, count(*) from movies_film group by genre_id order by genre_id"
    cursor.execute(raw)
    pair = cursor.fetchall()
  return pair


def home(request):
  genres = get_pair_genre_count_sql()
  context = {
    "genres" : genres,
    "films" : Film.objects.all(),
  }
  return render(request, "movies/home.html", context) 

def browse(request):
  genre = request.GET.get("genre", None)
  films = Film.objects.filter(genre=genre)
  context = {
    "genre" : genre,
    "films" : films,
  }
  return render(request, "movies/browse.html", context) 


def details(request, movie):
  pass

