from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
  path('', RedirectView.as_view(url='browse')),

  # http://127.0.0.1:8000/browse
  # http://127.0.0.1:8000/browse?search=<search>
  # http://127.0.0.1:8000/browse?genre=<genre>
  # http://127.0.0.1:8000/browse?section=<film|serie>
  path('browse', views.ViewBrowse.as_view(), name="view_browse"),

  # http://127.0.0.1:8000/favorites
  path('favorites', views.ViewTitleFavorites.as_view(), name="view_favorites"),

  # http://127.0.0.1:8000/title/<title_id>
  path('title/<int:title_id>', views.ViewTitleDetails.as_view(), name="view_details"),

  # http://127.0.0.1:8000/watch/<title-id>
  # http://127.0.0.1:8000/watch/<title-id>?s=<s-id>&e=<ep-id>
  path('watch/<int:title_id>', views.ViewWatchVideo.as_view(), name="view_watch"),
]