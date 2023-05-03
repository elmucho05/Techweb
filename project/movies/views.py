from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.db.models import Avg
from movies.models import Video, Film, TVSerie, Title, Episode
from profile.models import UserComment, UserFavorite, UserReview, UserHistory

class ViewWatchVideo(LoginRequiredMixin, View):
  def get(self, request, title_id):
    context = { "is_authorized" : True }
    
    title = get_object_or_404(Title, id=title_id)
    if title.type == 'serie':
      season = request.GET.get('s')
      ep     = request.GET.get('ep')
      serie   = get_object_or_404(TVSerie, title=title) 
      episode = get_object_or_404(Episode, serie=serie, num_season=season, num_ep=ep)
      context['video'] = episode.video
    else:
      film = get_object_or_404(Film, title=title)
      context['video'] = film.video

    try:
      UserHistory.objects.create(user=request.user, title=title)
    except:
      pass
  
    #messages.error(request, "Il servizio è disponibile solo per gli abbonati!")
    return render(request, 'movies/watch.html', context)

class ViewBrowse(View):
  def get(self, request):
    if len(request.GET) == 0:
      return view_home(request)
    
    section = request.GET.get("section", None)  # ?section=<film|serie>
    genre   = request.GET.get("genre",   None)  # ?genre=<genre>
    search  = request.GET.get("search",  None)  # ?search=<search>

    if search: return browse_search(request, search)
    if genre:  return browse_genre(request, genre)
    if section and section == 'film':  return browse_films(request)
    if section and section == 'serie': return browse_series(request)

def view_home(request):
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
    "section" : "film",
    "titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 

def browse_series(request):
  titles = Title.objects.filter(type="serie") 
  context = {
    "section" : "serie",
    "titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 

def browse_genre(request, genre):
  titles = Title.objects.filter(genre_id=genre)
  context = {
    "genre"  : genre,
    "titles" : titles,
  }
  return render(request, "movies/browse.html", context) 

def browse_search(request, search):
  titles = Title.objects.filter(name__icontains=search)
  messages.info(request, mark_safe(f'{len(titles)} risultati per <b>{search}</b>'))
  context = {
    "search"  : search,
    "titles"  : titles,
  }
  return render(request, "movies/browse.html", context) 


class ViewTitleDetails(View):

  def get(self, request, title_id):
    title = get_object_or_404(Title, id=title_id)
    
    is_favorite = request.user.is_authenticated and len(UserFavorite.objects.filter(user=request.user, title=title)) != 0
    can_vote    = request.user.is_authenticated and len(UserReview.objects.filter(user=request.user, title=title)) == 0

    reviews = UserReview.objects.filter(title=title)
    avg = reviews.aggregate(Avg('rating'))['rating__avg']

    context = {
      "title"       : title,
      "rating_avg"  : avg,
      "num_reviews" : len(reviews),
      "is_favorite" : is_favorite,
      "can_vote"    : can_vote,
      "comments"    : UserComment.objects.filter(title=title)
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
    # AJAX post request
    if action == 'add-vote':
      return add_vote(request, title_id)

def add_comment(request, title_id):
  text = request.POST.get('comment-text')
  try:
    UserComment.objects.create(user=request.user, title_id=title_id, text=text)
    messages.success(request, 'Commento aggiunto con successo!')
  except ValidationError as e:
    messages.error(request, str(e))
  return redirect('view_details', title_id=title_id)

def add_vote(request, title_id):
  rating = request.POST.get('rating')
  try:
    UserReview.objects.create(user=request.user, title_id=title_id, rating=rating)
  except Exception as e:
    return JsonResponse({'message' : str(e)}, status=400)
  messages.success(request, f'Hai votato con il punteggio di {rating}/5')
  return JsonResponse({}, status=200)


class ViewTitleFavorites(LoginRequiredMixin, View):
  login_url = '/authentication/login/'
  redirect_field_name = 'redirect_to'

  def get(self, request):
    context = { 
      'favorites' : UserFavorite.objects.filter(user=request.user)
    }
    return render(request, 'movies/favorites.html', context)

  # AJAX post request
  def post(self, request):
    action   = request.POST.get('action')
    title_id = request.POST.get('title_id')
    if action == 'add':
      return add_to_favorites(request, title_id)
    if action == 'remove':
      return remove_from_favorites(request, title_id)

def add_to_favorites(request, title_id):
  try:
    UserFavorite.objects.create(user=request.user, title_id=title_id)
  except ValidationError as e:
    return JsonResponse({'message' : str(e)}, status=400)
  return JsonResponse({}, status=200)

def remove_from_favorites(request, title_id):
  try:
    obj = UserFavorite.objects.get(user=request.user, title_id=title_id)
    obj.delete()
  except ValidationError as e:
    return JsonResponse({'message' : str(e)}, status=400)
  return JsonResponse({}, status=200)