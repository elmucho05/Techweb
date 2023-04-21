from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from user.models import User
from user.session import set_user_session_avatar_url, set_user_session_email, set_user_session_id, flush_user_session

def view_login(request):
  if request.method == "POST":
    email = request.POST.get("email")
    plain_password = request.POST.get("password")

    redirect_to = "home"
    try:
      user = User.objects.get(email=email)

      if not check_password(plain_password, user.password):
        raise ValidationError("")
      
      set_user_session_email(request, user.email)
      set_user_session_id(request, user.id)
      if user.avatar:
        set_user_session_avatar_url(request, str(user.avatar))
      
      messages.success(request, f'Login completato con successo')
    except (ObjectDoesNotExist, ValidationError):
      redirect_to = "view_login"
      messages.error(request, f'Email o password errati')

    return redirect(redirect_to)

  return render(request, "authentication/login.html")

def view_signup(request):
  if request.method == "POST":
    email = request.POST.get("email")
    plain_password = request.POST.get("password")
    encrypted_password = make_password(plain_password)

    redirect_to = "home"
    try:
      user = User.objects.create(email=email,password=encrypted_password)
      set_user_session_email(request, user.email)
      set_user_session_id(request, user.id)
      messages.success(request, f'Registrazione completata!') 
    except IntegrityError as e:
      messages.warning(request, f'Esiste già un utente con questa email')
      redirect_to = "view_signup"
    return redirect(redirect_to)
  
  return render(request, "authentication/signup.html")

def logout(request):
  flush_user_session(request)
  return redirect("home")