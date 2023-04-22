def set_user_session_email(request, email):
  request.session["user_email"] = email

def set_user_session_id(request, uid):
  request.session["user_id"] = uid

def set_user_session_avatar_url(request, avatar_url):
  request.session["user_avatar_url"] = avatar_url

def flush_user_session(request):
  request.session.flush()
