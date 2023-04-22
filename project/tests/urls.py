from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/tests/create-user
  path("create-user/", views.test_create_user, name="test_create_user"),

]