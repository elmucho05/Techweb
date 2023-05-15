from django.forms import ModelForm

from movies.models import Title, Video, Film, Thumb

""" Model Thumb """
class FormThumb(ModelForm):
  class Meta:
    model = Thumb
    fields = "__all__"
    labels = {
      'src' : "Seleziona l'immagine copertina"
    }


""" Model Video """
class FormVideo(ModelForm):
  class Meta:
    model = Video
    fields = "__all__"
    labels = {
      'src' : "Seleziona il file video",
      'duration' : 'Durata'

    }


""" Model Title """
class FormTitle(ModelForm):
  class Meta:
    model = Title
    fields = "__all__"
    exclude = ['thumb'] # exclude Foreign Key 
    labels = {
      'name' : 'Nome del film',
      'release_date' : 'Data di uscita',
      'description' : 'Descrizione',
      'type' : 'Tipo'
    }


""" Model Film """
class FormFilm(ModelForm):
  class Meta:
    model = Film
    fields = "__all__"
    exclude = ['title', 'video'] # exclude Foreign Key

    labels = {
      'director' : 'Regista'
    }



