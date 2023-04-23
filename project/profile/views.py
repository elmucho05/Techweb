from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponseBadRequest
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


from .models import UserProfile



class ViewProfile(LoginRequiredMixin, View):
  login_url = '/authentication/login/'
  redirect_field_name = 'redirect_to'
  
  def get(self, request, uid):
    try:
      user = User.objects.get(id=uid)
    except:
      return HttpResponseBadRequest(f"Invalid user")
    context = { 'user' : user }
    return render(request, "user/profile.html", context)



def view_update_user_avatar(request, uid):
  try:
    user = User.objects.get(id=uid)
  except:
    return HttpResponseBadRequest(f"Invalid user")
  
  avatar = request.FILES.get("fileAvatar")
  user.avatar = avatar
  user.save()
  #set_user_session_avatar_url(request, str(user.avatar))
  messages.success(request, "Immagine profilo aggiornata!")
  return redirect('view_profile', uid=uid)

def view_update_user_password(request, uid):
  old_password = request.POST.get('old-password')
  new_password = request.POST.get('new-password')

  messages.error(request, "Password non valida!")
  return redirect('view_profile', uid=uid)


