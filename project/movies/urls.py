from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/browse
  # http://127.0.0.1:8000/browse?search=<search>
  # http://127.0.0.1:8000/browse?genre=<genre>
  # http://127.0.0.1:8000/browse?section=<film|serie>
  path('browse', views.view_browse, name="view_browse"),

  # http://127.0.0.1:8000/favorites
  path('favorites', views.ViewTitleFavorites.as_view(), name="view_favorites"),

  # http://127.0.0.1:8000/title/<title_id>
  path('title/<int:title_id>', views.ViewTitleDetails.as_view(), name="view_details"),

  # http://127.0.0.1:8000/watch/<video_id>
  path('watch/<int:video_id>', views.view_watch, name="view_watch"),
]