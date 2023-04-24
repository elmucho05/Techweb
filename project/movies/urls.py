from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/browse/
  # http://127.0.0.1:8000/browse/?search=<search>
  # http://127.0.0.1:8000/browse/?genre=<genre>
  # http://127.0.0.1:8000/browse/?section=<film|serie>
  path('browse/', views.view_browse, name="view_browse"),

  # http://127.0.0.1:8000/title/<title_id>
  path('title/<title_id>', views.view_details, name="view_details"),

  # http://127.0.0.1:8000/watch/<video_id>
  path('watch/<video_id>', views.view_watch, name="view_watch"),
]