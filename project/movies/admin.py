from django.contrib import admin

from .models import Genre, Film, TVSerie

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(TVSerie)