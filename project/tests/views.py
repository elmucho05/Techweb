from django.http import HttpResponse
from django.contrib.auth.models import User

def test_create_user(request):
  try:
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
  except Exception as e:
    return HttpResponse(str(e))
  return HttpResponse(f"Account created!")

    
  

