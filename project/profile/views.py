from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.utils.html import strip_tags

from .models import UserProfile

class ViewProfile(LoginRequiredMixin, View):
  login_url = '/authentication/login/'
  redirect_field_name = 'redirect_to'
  
  def get(self, request):
    user_profile = UserProfile.objects.get(user=request.user)
    form = PasswordChangeForm(request.user)
    context = { 
      'update_password_form' : form,
      'user_profile' : user_profile,
    }
    return render(request, "user/profile.html", context)

  def post(self, request):
    action = request.GET.get('action')

    if action == 'update-password':
      update_user_password(request)
    
    elif action == 'update-avatar':
      update_user_avatar(request)

    return redirect('view_profile')

def update_user_password(request):
  form = PasswordChangeForm(user=request.user, data=request.POST)
  if form.is_valid():
    user = form.save()
    update_session_auth_hash(request, user)
    messages.success(request,'Password aggiornata con successo!')
  else:
    for e in form.errors.values():
      messages.error(request,f'{strip_tags(e)}')
  
def update_user_avatar(request):
  user_profile = UserProfile.objects.get(user=request.user)
  avatar = request.FILES.get("fileAvatar")
  user_profile.avatar = avatar
  user_profile.save()
  messages.success(request, "Immagine profilo aggiornata!")
    


