from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View

from .forms import RegistrationForm

class ViewLogin(View):
  form = AuthenticationForm()
  context = { 'form': form }

  def get(self, request):
    print(request.get_full_path())
    return render(request, "authentication/login.html", self.context)

  def post(self, request):
    self.form = AuthenticationForm(request.POST, data=request.POST)
    username = self.form.data.get('username')
    password = self.form.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      
      #?redirect_to=/u/7/profile
      redirect_to = request.GET.get('redirect_to', 'view_browse')
      messages.success(request, f'Login completato con successo')
      return redirect(redirect_to)
    
    messages.error(request, f'Username o password errati')
    return redirect('view_login')

class ViewSignUp(View):
  form = RegistrationForm()
  context = { 'form': form }

  def get(self, request):
    return render(request, "authentication/signup.html", self.context)

  def post(self, request):
    self.form = RegistrationForm(request.POST)

    if self.form.is_valid():
      self.form.save()
      messages.success(request, f'Registrazione completata!') 
      return redirect('view_browse')
    
    return redirect('view_signup')


def view_logout(request):
  logout(request)
  return redirect("view_browse")
  