from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForm


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
