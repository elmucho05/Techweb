from django.shortcuts import render
from .models import Genre

def home(request):
  # search_query = request.GET.get("search", None)
  genres = Genre.objects.all()
  context = {"genres" : genres}
  return render(request, "movies/home.html", context) 


