from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def login(request):
  if request.method == "POST":
    messages.success(request, 'success')
    return redirect("login")
  return render(request, "authentication/login.html")



def signup(request):
  if request.method == "POST":
    messages.warning(request, 'warning')
    return redirect("signup")
  return render(request, "authentication/signup.html")