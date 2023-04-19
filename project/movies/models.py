from django.db import models
from django.core.validators import FileExtensionValidator

class Genre(models.Model):
  name = models.CharField(primary_key=True, max_length=30)

  def __str__(self) -> str:
    return self.name


"""
rappresenta un oggetto video con
- id          identificatore
- src         sorgente del video
- duration    durata del video
"""
class Video(models.Model):
  id        = models.BigAutoField(primary_key=True)
  src       = models.FileField(upload_to='videos',null=True, 
                  validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  duration  = models.IntegerField()

  def __str__(self) -> str:
    return str(self.src) 

"""
rappresenta un oggetto thumb con
- id    identificatore
- src   sorgente dell'immagine
"""
class Thumb(models.Model):
  id  = models.BigAutoField(primary_key=True)
  src = models.ImageField(upload_to='thumbs', null=True, 
          validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','svg'])])
  
  def __str__(self) -> str:
    return str(self.src) 


"""
classe base da cui ereditano Film e TVSerie
- id            identificatore
- name          nome del film/serie tv
- release_date  data di rilascio del film/serie tv
- description   descrizione del film/serie tv
- thumb         copertina del film/serie tv
- genre         genere del film/serie tv
- type          distingue il titolo da film o serie tv
"""
class Title(models.Model):
  id            = models.BigAutoField(primary_key=True)
  name          = models.CharField(max_length=100)
  release_date  = models.DateField()
  description   = models.TextField()
  thumb         = models.ForeignKey(Thumb, null=True, on_delete=models.SET_NULL)
  genre         = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
  type          = models.CharField(max_length=5, choices=[('film', 'film'), ('serie', 'serie')])

  def __str__(self) -> str:
    return self.name


"""
la classe Film eredita da Title e aggiunge degli attributi
- director    regista del film
- video       riferimento al video
"""
class Film(models.Model):
  title    = models.OneToOneField(Title, on_delete=models.CASCADE, primary_key=True)
  director = models.CharField(max_length=100, null=True)
  video    = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)

  def __str__(self) -> str:
    return str(self.title) 


"""
la classe TVSerie eredita da Title e aggiunge un attributo
- seasons       numero di stagioni
"""
class TVSerie(models.Model):
  title   = models.OneToOneField(Title, on_delete=models.CASCADE, primary_key=True)
  seasons = models.IntegerField()

  def __str__(self) -> str:
    return str(self.title) 


"""
la class Episode rappresenta un oggetto di tipo episodio
- name_ep     nome dell'episodio
- num_ep      numero dell'episodio
- num_season  numero della stagione
- tv          riferimento alla serie tv
- video       riferimento al video
"""
class Episode(models.Model):
  name_ep     = models.CharField(max_length=50, default=None)
  num_ep      = models.IntegerField()
  num_season  = models.IntegerField()
  serie       = models.ForeignKey(TVSerie, on_delete=models.CASCADE)
  video       = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
  def __str__(self) -> str:
    return f'S{self.num_season} E{self.num_ep} {self.name_ep}'
  

