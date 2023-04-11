from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  # search_query = request.GET.get("search", None)
  return render(request, "movies/index.html") 