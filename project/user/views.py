from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from .models import User
from .session import set_user_session_avatar_url



def view_profile(request, uid):
  try:
    user = User.objects.get(id=uid)
  except:
    return HttpResponseBadRequest(f"Invalid user")
  context = { 'user' : user }
  return render(request, "user/profile.html", context)

@require_http_methods(["POST"])
def view_update_user_avatar(request, uid):
  try:
    user = User.objects.get(id=uid)
  except:
    return HttpResponseBadRequest(f"Invalid user")
  
  avatar = request.FILES.get("fileAvatar")
  user.avatar = avatar
  user.save()
  set_user_session_avatar_url(request, str(user.avatar))
  return redirect('view_profile', uid=uid)

