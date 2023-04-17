from django.shortcuts import render
from django.http import HttpResponseBadRequest

from .models import User

def profile(request, uid):
  try:
    user = User.objects.get(id=uid)
  except:
    return HttpResponseBadRequest(f"invalid user id {uid}")

  context = { 'user' : user }
  return render(request, "user/profile.html", context)

