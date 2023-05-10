from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash, authenticate, logout
from django.contrib import messages
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST

from .models import UserProfile, UserComment, UserReview, UserHistory, SubscriptionType, UserSubscription

class ViewProfile(LoginRequiredMixin, View):
  login_url = '/authentication/login/'
  redirect_field_name = 'redirect_to'
  
  def get(self, request):
    context = { 
      'user_profile' : UserProfile.objects.get(user=request.user),
      'reviews'      : UserReview.objects.filter(user=request.user),
      'history'      : UserHistory.objects.filter(user=request.user),
      'comments'     : UserComment.objects.filter(user=request.user),
    }
    return render(request, "profile/account.html", context)


@require_POST
def update_user_avatar(request):
  user_profile = UserProfile.objects.get(user=request.user)
  avatar = request.FILES.get("fileAvatar")
  user_profile.avatar = avatar
  user_profile.save()
  messages.success(request, "Immagine profilo aggiornata!")
  return redirect('view_profile')


@require_POST # AJAX POST request
def delete_user_comment(request):
  comment_id = request.POST.get('comment-id')

  try:
    UserComment.objects.get(id=comment_id).delete()
  except Exception as e:
    return JsonResponse({'message' : str(e)}, status=400)

  messages.success(request, 'Commento eliminato con successo')
  return JsonResponse({}, status=200)


class ViewUpdatePassword(View):
  def get(self, request):
    context = { 'form' :  PasswordChangeForm(request.user) }
    return render(request, "profile/update-password.html", context) 

  def post(self, request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request,'Password aggiornata con successo!')
    else:
      for e in form.errors.values():
        messages.error(request,f'{strip_tags(e)}')
    return redirect('view_update_password')

class ViewDeleteAccount(View):
  def get(self, request):
    context = { 'form' : AuthenticationForm()}
    return render(request, "profile/delete-account.html", context) 

  def post(self, request):
    form = AuthenticationForm(request.POST, data=request.POST)
    if form.is_valid():
      username = form.data.get('username')
      password = form.data.get('password')
      user = authenticate(username=username, password=password)
      if user is None:
        messages.error(request, f'Crendenziali non corrette') 
        return redirect('view_delete_account')
  
      user.delete()
      logout(request)
      messages.success(request, f'Account eliminato con successo!')
      return redirect('view_browse')
        
    for e in form.errors.values():
      messages.error(request, f'{strip_tags(e)}')
    return redirect('view_delete_account')

class ViewSubscription(View):
  def get(self, request):
    try:
      user_sub = UserSubscription.objects.get(user=request.user)
    except:
      user_sub = None
    context = {
      'subscription_list' : SubscriptionType.objects.all(),
      'user_subscription' : user_sub,
    }
    return render(request, "profile/subscription.html", context) 


  def post(self, request): # AJAX POST request
    action   = request.POST.get('action')
    
    if action == 'add-new-subscription':
      return new_user_subscription(request)
    
    if action == 'deactivate-subscription':
      return deactivate_user_subscription(request)
    
    if action == 'activate-subscription':
      return activate_user_subscription(request)

    if action == 'modify-subscription':
      return modify_user_subscription(request)

  
def new_user_subscription(request):
  sub_type = request.POST.get('sub-type')
  UserSubscription.objects.create(user=request.user, subscription_id=sub_type)
  messages.success(request, f"Abbonamento creato con successo!")
  return JsonResponse({}, status=200)

def deactivate_user_subscription(request):
  us = UserSubscription.objects.get(user=request.user)
  us.is_active = False
  us.save()
  messages.success(request, f'Abbonamento disattivato con successo!')
  return JsonResponse({}, status=200)

def activate_user_subscription(request):
  us = UserSubscription.objects.get(user=request.user)
  us.is_active = True
  us.save()
  messages.success(request, f'Abbonamento attivato con successo!')
  return JsonResponse({}, status=200)

def modify_user_subscription(request):
  sub_type = request.POST.get('sub-type')
  subscription = SubscriptionType.objects.get(type=sub_type)
  us = UserSubscription.objects.get(user=request.user)
  us.subscription = subscription
  us.save()
  messages.success(request, f'Abbonamento modificato con successo!')
  return JsonResponse({}, status=200)

