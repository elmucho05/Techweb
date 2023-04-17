from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from user.models import User

def login(request):
  if request.method == "POST":
    email  = request.POST.get("email")
    plain_password = request.POST.get("password")

    redirect_to = "home"
    try:
      user = User.objects.get(email=email)

      if not check_password(plain_password, user.password):
        raise ValidationError("")
      
      request.session["user_email"] = user.email
      request.session["user_id"] = user.id
      if user.avatar:
        request.session["user_avatar_url"] = str(user.avatar) 
      
      messages.success(request, f'Login completato con successo')
    except (ObjectDoesNotExist, ValidationError):
      redirect_to = "login"
      messages.error(request, f'Email o password errati')

    return redirect(redirect_to)

  return render(request, "authentication/login.html")

def signup(request):
  if request.method == "POST":
    email = request.POST.get("email")
    plain_password = request.POST.get("password")
    encrypted_password = make_password(plain_password)

    redirec_to = "home"
    try:
      user = User.objects.create(email=email, password=encrypted_password)
      
      request.session["user_email"] = user.email
      request.session["user_id"] = user.id
      messages.success(request, f'Registrazione completata!') 
    except IntegrityError as e:
      messages.warning(request, f'Esiste già un utente con questa email')
      redirec_to = "signup"
    return redirect(redirec_to)
  
  return render(request, "authentication/signup.html")

def logout(request):
  request.session.flush()
  return redirect("home")