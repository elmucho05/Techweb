from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import Film, TVSerie, Title

def home(request):
  titles = Title.objects.all()
  genres = titles.values("genre_id").distinct()
  context = {
    "titles" : titles,
    "genres" : genres,
  }
  return render(request, "movies/home.html", context) 


def view_films(request):
  titles = Title.objects.filter(type='film')
  genres = titles.values("genre_id").distinct()
  context = {
    "titles" : titles,
    "genres" : genres,
  }
  return render(request, "movies/home.html", context) 

def view_series(request):
  titles = Title.objects.filter(type='serie')
  genres = titles.values("genre_id").distinct()
  context = {
    "titles" : titles,
    "genres" : genres,
  }
  return render(request, "movies/home.html", context) 





def view_browse(request):
  genre  = request.GET.get("genre", None)
  search = request.GET.get("search", None)
  titles = []

  if search:
    titles = Title.objects.filter(name__icontains=search)
    messages.info(request, mark_safe(f'{len(titles)} risultati per <b>{search}</b>'))
  elif genre:
    titles = titles.objects.filter(genre=genre, type=type)
    
  context = {
    "genre" : genre,
    "search" : search,
    "titles" : titles,
  }
  return render(request, "movies/browse.html", context) 

def view_details(request, id):
  title = Title.objects.get(id=id)
  film  = None
  serie = None

  if title.type == 'film':
    film  = Film.objects.get(title_id=id) 
  else:
    serie = TVSerie.objects.get(title_id=id)

  context = { 
    "title" : title, 
    "film"  : film,
    "serie" : serie,
  }
  return render(request, "movies/details.html", context)


def view_watch(request, id):
  type   = request.GET.get('type', None)
  season = request.GET.get('season', None)
  ep     = request.GET.get('episode', None)



  return HttpResponse("hello world")