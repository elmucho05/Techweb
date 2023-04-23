from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.FileField(upload_to='avatars', null=True, 
    validators=[FileExtensionValidator(allowed_extensions=['jpg','png','svg'])])

  def __str__(self) -> str:
    return self.user




  

