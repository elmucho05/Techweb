from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
from movies.models import Title

#[user] simone:modena99
#[user] james:jamesbond123
#[user] kevin:kevinlebron

"""
rappresenta le informazioni aggiuntive relative ad un utente:
- user deve essere UNIQUE
"""
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.FileField(upload_to='avatars', null=True, 
    validators=[FileExtensionValidator(allowed_extensions=['jpg','png','svg'])])

  def __str__(self) -> str:
    return self.user.username


"""
rappresenta i commenti degli utenti sotto ai titoli:
un utente può commentare più volte lo stesso titolo
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
rappresenta la lista dei titoli preferiti di un utente:
un utente non può mettere nei preferiti lo stesso titolo più volte
(il controllo avviene anche nella parte di FE)
"""
class UserFavorite(models.Model):
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.ForeignKey(Title, on_delete=models.CASCADE)
  
  class Meta:
    unique_together = (("user", "title"),)

"""
rappresenta le recensioni fatte da un utente:
un utente non può recensire lo stesso titolo più volte
(il controllo avviene anche nella parte di FE)
- rating è un valore intero che assume valori 1-5
"""
class UserReview(models.Model):
  user   = models.ForeignKey(User, on_delete=models.CASCADE)
  title  = models.ForeignKey(Title, on_delete=models.CASCADE)
  rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

  class Meta:
    unique_together = (("user", "title"),)


"""
rappresenta la history dei film visti da un utente
"""
class UserHistory(models.Model):
  user   = models.ForeignKey(User, on_delete=models.CASCADE)
  title  = models.ForeignKey(Title, on_delete=models.CASCADE)
  date   = models.DateField(default=timezone.now)

  class Meta:
    unique_together = (("user", "title"),)



"""
rappresenta i vari tipi di abbonamento disponibili
- annuale
- mensile
"""
class SubscriptionType(models.Model):
  type = models.CharField(max_length=7, choices=(('mensile','mensile'), ('annuale', 'annuale')), primary_key=True)
  cost = models.DecimalField(max_digits=5, decimal_places=2)
  
  def __str__(self):
    return f'{self.type}: €{self.cost}'


"""
rappresenta l'abbonamento collegato ad un utente per vedere i titoli
"""
class UserSubscription(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  subscription = models.OneToOneField(SubscriptionType, on_delete=models.CASCADE)
  
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.user}:{self.subscription}'

  
  