from django.db import models
from django.core.validators import FileExtensionValidator

class Genre(models.Model):
  name = models.CharField(primary_key=True, max_length=30)

  def __str__(self) -> str:
    return self.name


class Film(models.Model):
  name          = models.CharField(max_length=100)
  director      = models.CharField(max_length=100)
  release_date  = models.DateField()
  description   = models.TextField()
  thumb         = models.ImageField(upload_to='thumbs')
  videosrc      = models.FileField(upload_to='videos',null=True, 
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  duration      = models.IntegerField()
  genre         = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

  def __str__(self) -> str:
    return self.name



# class TVSerie(models.Model):
#   pass


  
