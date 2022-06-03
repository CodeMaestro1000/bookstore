from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.views.generic import CreateView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
