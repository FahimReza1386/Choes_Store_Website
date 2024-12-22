from django.urls import path
from . import views

urlpatterns =[
    path("register/" , views.UserRegister.as_view() , name="UserRegister"),
    path("login/" , views.UserLogin.as_view() , name="UserLogin"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    ]