from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("home1", views.home1, name="signup"),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('register', views.reg_user)

]
