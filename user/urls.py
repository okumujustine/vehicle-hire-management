from django.urls import path

from user.views import login, siginup

app_name = "user_app"

urlpatterns = [
    path("login/", login, name="user_login_url"),
    path("siginup/", siginup, name="user_register_url"),
]
