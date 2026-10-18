from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),   # if you have signup
    path("login/", views.login_view, name="login"),      # if you have login
    path("", views.dashboard_view, name="home"),             # root of accounts → dashboard
]
