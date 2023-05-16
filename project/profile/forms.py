from django import forms
from django.forms import ModelForm
import datetime

from movies.models import Title, Video, Film, Thumb

""" Model Thumb """
class FormThumb(ModelForm):
  class Meta:
    model = Thumb
    fields = "__all__"
    labels = {
      'thumb_src' : "Seleziona l'immagine copertina"
    }


""" Model Video """
class FormVideo(ModelForm):
  class Meta:
    model = Video
    fields = "__all__"
    labels = {
      'video_src' : "Seleziona il file video",
      'duration' : 'Durata (in minuti)'
    }


""" Model Title """
class FormTitle(ModelForm):
  class Meta:
    model = Title
    fields = "__all__"
    exclude = ['thumb'] # exclude Foreign Key
    labels = {
      'name' : 'Nome del film',
      'release_date' : 'Data di uscita (AAAA-MM-GG)',
      'description' : 'Descrizione',
      'type' : 'Tipo'
    }
    widgets = {'type': forms.HiddenInput()}
    

""" Model Film """
class FormFilm(ModelForm):
  class Meta:
    model = Film
    fields = "__all__"
    exclude = ['title', 'video'] # exclude Foreign Key

    labels = {
      'director' : 'Regista'
    }



