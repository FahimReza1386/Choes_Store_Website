from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class UserRegister(CreateView):
    template_name = "Accounts/Register.html"
    success_url="/"
    form_class=UserRegisterForm
    
    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)
        return super().form_valid(form)
    

class UserLogin(LoginView):
    template_name = "Accounts/Login.html"
    redirect_authenticated_user = "/"
    fields=["email", "password"]
    success_url="/"


class UserLogout(LogoutView):
    success_url = "/"