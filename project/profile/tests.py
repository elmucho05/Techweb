from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class TestProfile(TestCase):

  def setUp(self):
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    User.objects.create_user('doe', 'doe@thebeatles.com', 'doepassword')

  def test_update_password(self):
    credentials = {'username':'john', 'password':'johnpassword'}
    
    """authenticate with right credentials"""
    user = User.objects.get(username='john')
    self.assertIsNotNone(authenticate(**credentials), user)

    """update password"""
    user.set_password('newjohnpassword')
    user.save()

    """trying to authenticate with old credentials"""
    self.assertIsNone(authenticate(**credentials), user)
