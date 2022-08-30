from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('register', views.reg_user)

]
