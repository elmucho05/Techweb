from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import Video, Film, TVSerie, Title, Episode

def home(request):
  titles = Title.objects.all()
  genres = titles.values("genre_id").distinct()
  context = {
    "titles" : titles,
    "genres" : genres,
  }
  return render(request, "movies/home.html", context) 

def view_browse(request):
  section = request.GET.get("section", None)  # film|serie
  genre   = request.GET.get("genre", None)    # <title_genre>
  search  = request.GET.get("search", None)   # <title_name>
  titles  = []
  
  # http://127.0.0.1:8000/browse?search=<search>
  if search:
    titles = Title.objects.filter(name__icontains=search)
    messages.info(request, mark_safe(f'{len(titles)} risultati per <b>{search}</b>'))
  
  # http://127.0.0.1:8000/browse?genre=<genre>
  elif genre:
    titles = Title.objects.filter(genre_id=genre)
  
  # http://127.0.0.1:8000/browse?section=<film|serie>
  elif section:
    titles = Title.objects.filter(type=section) 

  context = {
    "genre"   : genre,
    "search"  : search,
    "section" : section,
    "titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 

def view_details(request, title_id):
  title = Title.objects.get(id=title_id)
  film  = None
  serie = None
  episodes = []
  seasons_range = None

  if title.type == 'film':
    film  = Film.objects.get(title_id=title_id) 
  else:
    serie = TVSerie.objects.get(title_id=title_id)
    episodes = Episode.objects.filter(serie=serie).order_by('num_season', 'num_ep')
    seasons_range = range(1, serie.seasons + 1)

  context = { 
    "title" : title, 
    "film"  : film,
    "serie" : serie,
    "episodes" : episodes,
    "seasons_range" : seasons_range,
  }
  return render(request, "movies/details.html", context)

def view_watch(request, video_id):
  try:
    video = Video.objects.get(id=video_id)
  except:
    return HttpResponseNotFound("video non trovato")

  context = { "video" : video }
  return render(request, 'movies/watch.html', context)