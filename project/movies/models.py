from django.db import models
from django.core.validators import FileExtensionValidator

class Genre(models.Model):
  name = models.CharField(primary_key=True, max_length=30)

  def __str__(self) -> str:
    return self.name


"""
rappresenta la classe base di un video utilizzata per Film e serie TV
-id         identificativo 
-name       nome film, nome episodio serie TV
-thumb      copertina del film, copertina dell'episodio serie TV
-src        percorso del file video 
-duration   durata film, durata episodio serie TV
"""
class Video(models.Model):
  id           = models.BigAutoField(primary_key=True)
  name         = models.CharField(max_length=100)
  description  = models.TextField()
  thumb        = models.ImageField(upload_to='thumbs', null=True, 
                  validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','svg'])])
  src          = models.FileField(upload_to='videos',null=True, 
                  validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  duration     = models.IntegerField()


"""
un film è visto come un oggetto video con proprietà aggiuntive:
-director       regista del film
-release_date   data di rilascio del film
-genre          genere del film
"""
class Film(Video):
  director      = models.CharField(max_length=100)
  release_date  = models.DateField()
  genre         = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

  def __str__(self) -> str:
    return self.name



"""
una serie TV e vista come una collezione di video (episodi) ordinata per stagioni
ed episodi
-name           nome della serie TV
-release_date   data di rilascio della serie TV
-seasons        numero di stagioni
-thumb          copertina della serie TV
"""
class TVSerie(models.Model):
  id            = models.BigAutoField(primary_key=True)
  name          = models.CharField(max_length=100)
  release_date  = models.DateField()
  seasons       = models.IntegerField()
  description   = models.TextField()
  thumb         = models.ImageField(upload_to='thumbs')
  genre         = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

  def __str__(self) -> str:
    return self.name
  

  """
un episodio eredita le caratteristiche di un Video ma possiede
qualche attributo aggiuntivo
-id_ep      rappresenta il numero dell'episodio
-id_season  rappresenta il numero della stagione relativa
-tvserie    rappresenta il riferimento alla serie TV
"""
# class Episode(Video):
#   id_ep     = models.IntegerField()
#   id_season = models.IntegerField()
#   tvserie   = models.ForeignKey(TVSerie, on_delete=models.CASCADE)

#   def __str__(self) -> str:
#     return f'Episodio {self.id_ep}'
  
