from django.db import models
from django.core.validators import FileExtensionValidator

class Genre(models.Model):
  name = models.CharField(primary_key=True, max_length=30)

  def __str__(self) -> str:
    return self.name


"""
rappresenta un video
- id          identificatore
- src         sorgente del video
- duration    durata del video
"""
class Video(models.Model):
  id        = models.BigAutoField(primary_key=True)
  video_src = models.FileField(upload_to='videos',null=True, 
                validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  duration  = models.PositiveIntegerField()

  def __str__(self) -> str:
    return str(self.video_src)


"""
rappresenta la copertina di un titolo
- id    identificatore
- src   sorgente dell'immagine
"""
class Thumb(models.Model):
  id  = models.BigAutoField(primary_key=True)
  thumb_src = models.ImageField(upload_to='thumbs', null=True, 
          validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','svg'])])
  
  def __str__(self) -> str:
    return str(self.thumb_src) 


"""
classe base da cui ereditano Film e TVSerie
- name          nome del film/serie tv
- release_date  data di rilascio del film/serie tv
- description   descrizione del film/serie tv
- thumb         copertina del film/serie tv
- genre         genere del film/serie tv
- type          distingue il titolo da film o serie tv
- included      permette di distinguere i titoli che sono inclusi nell'abbonamento
- cost          [campo facoltativo] costo di noleggio di un titolo 
"""
class Title(models.Model):
  name          = models.CharField(max_length=100, unique=True)
  release_date  = models.DateField()
  description   = models.TextField()
  thumb         = models.ForeignKey(Thumb, null=True, on_delete=models.SET_NULL)
  genre         = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
  type          = models.CharField(max_length=5, choices=[('film', 'film'), ('serie', 'serie')])
  included      = models.BooleanField(default=True)
  cost          = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)

  def __str__(self) -> str:
    return self.name


"""
la classe Film eredita da Title e implementa attributi aggiuntivi
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
rappresenta un episodio legato ad una serie tv
la chiave primaria è composta da <ep, season, serie>
- name_ep     nome dell'episodio
- num_ep      numero dell'episodio
- num_season  numero della stagione
- serie       riferimento alla serie tv
- video       riferimento al video
"""
class Episode(models.Model):
  name_ep     = models.CharField(max_length=50, default=None)
  num_ep      = models.IntegerField()
  num_season  = models.IntegerField()
  serie       = models.ForeignKey(TVSerie, on_delete=models.CASCADE)
  video       = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)

  class Meta:
    unique_together = (("num_ep", "num_season", "serie"),)

  def __str__(self) -> str:
    return f'S{self.num_season} E{self.num_ep} {self.name_ep}'
  