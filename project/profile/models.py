from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from movies.models import Title

#[user] simonee:modena99
#[user] james:jamesbond123
#[user] kevin:kevinlebron

"""
rappresenta le informazioni aggiuntive relative ad un utente
"""
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.FileField(upload_to='avatars', null=True, 
    validators=[FileExtensionValidator(allowed_extensions=['jpg','png','svg'])])

  def __str__(self) -> str:
    return self.user.username


"""
rappresenta i commenti degli utenti sotto ai titoli 
- user    riferimento all'utente
- titolo  riferimento al titolo
- text    testo del commento
"""
class UserComment(models.Model):
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.ForeignKey(Title, on_delete=models.CASCADE)
  text  = models.TextField()

  def __str__(self) -> str:
    return f'{self.user}:{self.title}:{self.text}'
  

"""
rappresenta la lista dei titoli preferiti di un utente
"""
class UserFavorite(models.Model):
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.ForeignKey(Title, on_delete=models.CASCADE)
