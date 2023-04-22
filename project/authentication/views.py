from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from user.models import User
# from user.session import set_user_session_avatar_url, set_user_session_email, set_user_session_id, flush_user_session


class ViewLogin(View):
  template_name = "authentication/login.html"

  def get(self, request):
    return render(request, self.template_name)

  def post(self, request):
    email    = request.POST.get("email")
    password = request.POST.get("password")
    print(email, password)

    user = authenticate(email=email, password=password)

    redirect_to = 'home'
    if user:
      login(request, user)
      messages.success(request, f'Login completato con successo')
    else:
      redirect_to = 'view_login'
      messages.error(request, f'Username o password errati')
    return redirect(redirect_to)



class ViewSignUp(View):
  def get(self, request):
    return render(request, "authentication/signup.html")

  def post(self, request):
    email    = request.POST.get("email")
    username = request.POST.get("username")
    password = request.POST.get("password")

    redirect_to = "home"
    try:
      user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
      messages.success(request, f'Registrazione completata!') 
    except Exception as e:
      redirect_to = "view_signup"
      messages.error(request, f'{str(e)}')

    return redirect(redirect_to)


def logout(request):
  #request.session.flush()
  return redirect("home")
  