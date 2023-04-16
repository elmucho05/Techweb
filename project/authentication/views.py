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
      
      messages.success(request, f'Login completato con successo')
      request.session["user_email"] = user.email
      if user.avatar:
        request.session["user_avatar"] = str(user.avatar) 
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
      messages.success(request, f'Registrazione completata!') 
      request.session["user_email"] = user.email
    except IntegrityError as e:
      messages.warning(request, f'Esiste già un utente con questa email')
      redirec_to = "signup"
    return redirect(redirec_to)
  
  return render(request, "authentication/signup.html")

def logout(request):
  try:
    del request.session['user_email']
    del request.session["user_avatar_url"]
  except Exception:
    pass  

  return redirect("home")