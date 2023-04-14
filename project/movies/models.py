from django.db import models

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
  duration      = models.IntegerField()
  genre         = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

  def __str__(self) -> str:
    return self.name



# class TVSerie(models.Model):
#   pass


  
