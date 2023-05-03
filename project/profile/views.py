from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash, authenticate, logout
from django.contrib import messages
from django.utils.html import strip_tags

from .models import UserProfile, UserComment, UserReview, UserHistory

class ViewProfile(LoginRequiredMixin, View):
  login_url = '/authentication/login/'
  redirect_field_name = 'redirect_to'
  
  def get(self, request):
    context = { 
      'user_profile'         : UserProfile.objects.get(user=request.user),
      'update_password_form' : PasswordChangeForm(request.user),
      'delete_account_form'  : AuthenticationForm(),
      'reviews'              : UserReview.objects.filter(user=request.user),
      'history'              : UserHistory.objects.filter(user=request.user),
      'comments'             : UserComment.objects.filter(user=request.user),
    }
    return render(request, "user/profile.html", context)

  def post(self, request):
    action = request.GET.get('action')

    if action == 'update-password':
      return update_user_password(request)
    
    if action == 'update-avatar':
      return update_user_avatar(request)

    if action == 'delete-account':
      return delete_user_account(request)
    
    # AJAX post request
    if action == 'delete-comment':
      return delete_user_comment(request)
    
def update_user_password(request):
  form = PasswordChangeForm(user=request.user, data=request.POST)
  if form.is_valid():
    user = form.save()
    update_session_auth_hash(request, user)
    messages.success(request,'Password aggiornata con successo!')
  else:
    for e in form.errors.values():
      messages.error(request,f'{strip_tags(e)}')
  return redirect('view_profile')
  
def update_user_avatar(request):
  user_profile = UserProfile.objects.get(user=request.user)
  avatar = request.FILES.get("fileAvatar")
  user_profile.avatar = avatar
  user_profile.save()
  messages.success(request, "Immagine profilo aggiornata!")
  return redirect('view_profile')

def delete_user_account(request):
  form = AuthenticationForm(request.POST, data=request.POST)

  if form.is_valid():
    username = form.data.get('username')
    password = form.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
      messages.error(request, f'Crendenziali non corrette') 
      return redirect('view_profile')
 
    user.delete()
    logout(request)
    messages.success(request, f'Account eliminato con successo!')
    return redirect('view_browse')
      
  for e in form.errors.values():
    messages.error(request, f'{strip_tags(e)}')
  return redirect('view_profile')

def delete_user_comment(request):
  comment_id = request.GET.get('comment-id')

  try:
    UserComment.objects.get(id=comment_id).delete()
  except Exception as e:
    return JsonResponse({'message' : str(e)}, status=400)

  messages.success(request, 'Commento eliminato con successo')
  return JsonResponse({}, status=200)
  