from django.db import models
from django.core.validators import FileExtensionValidator

class User(models.Model):
  email    = models.CharField(max_length=320, primary_key=True)
  password = models.CharField(max_length=128) # hashed password
  avatar   = models.FileField(upload_to='avatars', null=True, 
              validators=[FileExtensionValidator(allowed_extensions=['jpg','png','svg'])])

  def __str__(self) -> str:
    return f"{self.email}"



# class Billing(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   firstname = ...
#   lastname = ...

#   address = ...
#   city = ...
#   country = ...
#   postcode = ...

#   phonenumber = ...
#   email = ...

  

