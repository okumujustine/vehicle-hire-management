from django.urls import path

from user.views import login, signup, logout_view

app_name = "user_app"

urlpatterns = [
    path("login/", login, name="user_login_url"),
    path("signup/", signup, name="user_register_url"),
    path("logout/", logout_view, name="user_logout_url")
]
