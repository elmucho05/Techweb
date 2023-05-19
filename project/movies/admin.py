from django.contrib import admin

from .models import Genre, Video, Thumb, Title, Film, TVSerie, Episode

admin.site.register(Genre)
admin.site.register(Video)
admin.site.register(Thumb)
admin.site.register(Title)
admin.site.register(Film)
admin.site.register(TVSerie)
admin.site.register(Episode)

