from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from movies.models import Video, Film, TVSerie, Title, Episode
from profile.models import UserComment, UserFavorite

def home(request):
  titles = Title.objects.all()
  genres = titles.values("genre_id").distinct()
  context = {
    "titles" : titles,
    "genres" : genres,
  }
  return render(request, "movies/home.html", context)

def browse_films(request):
  titles = Title.objects.filter(type="film") 
  context = {
    "browse_section" : "film",
    "browse_titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 

def browse_series(request):
  titles = Title.objects.filter(type="serie") 
  context = {
    "browse_section" : "serie",
    "browse_titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 

def browse_genre(request, genre):
  titles = Title.objects.filter(genre_id=genre)
  context = {
    "browse_genre"  : genre,
    "browse_titles" : titles,
  }
  return render(request, "movies/browse.html", context) 

def browse_search(request, search):
  titles = Title.objects.filter(name__icontains=search)
  messages.info(request, mark_safe(f'{len(titles)} risultati per <b>{search}</b>'))
  context = {
    "browse_search"  : search,
    "browse_titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 

def view_browse(request):
  if len(request.GET) > 0:
    section = request.GET.get("section", None)  # ?section=<film|serie>
    genre   = request.GET.get("genre",   None)  # ?genre=<genre>
    search  = request.GET.get("search",  None)  # ?search=<search>

    if search: return browse_search(request, search)
    if genre:  return browse_genre(request, genre)
    if section and section == 'film':  return browse_films(request)
    if section and section == 'serie': return browse_series(request)

  return home(request)

def view_watch(request, video_id):
  video = get_object_or_404(Video, id=video_id)
  context = { 
    "video" : video,
    "is_authorized" : True,
  }
  messages.error(request, "Il servizio è disponibile solo per gli abbonati!")
  return render(request, 'movies/watch.html', context)


class ViewTitleDetails(View):

  def get(self, request, title_id):
    title = get_object_or_404(Title, id=title_id)
    
    is_favorite = True
    try:
      UserFavorite.objects.get(user=request.user, title=title)
    except:
      is_favorite = False

    comments = UserComment.objects.filter(title=title)
    context = {
      "title" : title,
      "is_favorite" : is_favorite,
      "comments" : comments
    }

    if title.type == 'film':
      film  = Film.objects.get(title_id=title_id) 
      context["film"] = film
    else:
      serie = TVSerie.objects.get(title_id=title_id)
      episodes = Episode.objects.filter(serie=serie).order_by('num_season', 'num_ep')
      seasons_range = range(1, serie.seasons + 1)
      context["serie"] = serie
      context["episodes"] = episodes
      context["seasons_range"] = seasons_range
    return render(request, "movies/details.html", context)

  def post(self, request, title_id):
    action = request.GET.get('action')
    if action == 'add-comment':
      return add_comment(request, title_id)
    if action == 'add-to-favorites':
      return add_to_favorites(request, title_id)

    return redirect('view_details', title_id=title_id)

def add_comment(request, title_id):
  text = request.POST.get('comment-text')
  try:
    UserComment.objects.create(user=request.user, title_id=title_id, text=text)
    messages.success(request, 'Commento aggiunto con successo!')
  except ValidationError as e:
    messages.error(request, str(e))
  return redirect('view_details', title_id=title_id)

def add_to_favorites(request, title_id):
  try:
    UserFavorite.objects.create(user=request.user, title_id=title_id)
  except ValidationError as e:
    return JsonResponse({'message' : str(e)}, status=400)
  return JsonResponse({}, status=200)
  
  

class ViewTitleFavorites(LoginRequiredMixin, View):
  login_url = '/authentication/login/'
  redirect_field_name = 'redirect_to'
  
  def get(self, request):
    titles = []
    for t in UserFavorite.objects.filter(user=request.user):
      titles.append(t.title)

    context = { 'titles' : titles }
    return render(request, 'movies/favorites.html', context)

  def post(self, request):
    pass


