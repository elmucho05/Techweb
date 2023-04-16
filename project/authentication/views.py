from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from user.models import User

def login(request):
  if request.method == "POST":
    email    = request.POST.get("email")
    plain_password = request.POST.get("password")

    try:
      user = User.objects.get(email=email)

      if not check_password(plain_password, user.password):
        raise ValidationError("")
      
      messages.success(request, f'Login completato con successo')
    except (ObjectDoesNotExist, ValidationError):
      messages.warning(request, f'Email o password errati')

    return redirect("login")
  
  return render(request, "authentication/login.html")



def signup(request):
  if request.method == "POST":
    email = request.POST.get("email")
    plain_password = request.POST.get("password")
    encrypted_password = make_password(plain_password)

    try:
      User.objects.create(email=email, password=encrypted_password)
      messages.success(request, f'Registrazione completata con successo') 
    except IntegrityError as e:
      messages.warning(request, f'IntegrityError: esiste già un utente con questa email') 
    return redirect("signup")
  
  return render(request, "authentication/signup.html")