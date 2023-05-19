from django.urls import path

from . import views

urlpatterns = [
  # http://127.0.0.1:8000/profile
  path('', views.ViewProfile.as_view(), name="view_profile"),

  # http://127.0.0.1:8000/profile/update-avatar
  # ONLY post
  path('update-avatar', views.update_user_avatar, name="view_update_avatar"),

  # http://127.0.0.1:8000/profile/delete-comment
  # ONLY post, AJAX request
  path('delete-comment', views.delete_user_comment, name="view_delete_comment"),

  # http://127.0.0.1:8000/profile/update-password
  path('update-password', views.ViewUpdatePassword.as_view(), name="view_update_password"),

  # http://127.0.0.1:8000/profile/subscription
  path('subscription', views.ViewSubscription.as_view(), name="view_subscription"),

  # http://127.0.0.1:8000/profile/your-purchases
  path('your-purchases', views.ViewPurchase.as_view(), name="view_purchases"),

  # http://127.0.0.1:8000/profile/upload-title
  path('upload-film', views.ViewUploadFilm.as_view(), name="view_upload_film"),

  # http://127.0.0.1:8000/delete-account
  path('delete-account', views.ViewDeleteAccount.as_view(), name="view_delete_account"),
]