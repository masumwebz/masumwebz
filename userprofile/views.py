from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from .forms import SignUpForm





# signup view
class SignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('dashboard')
    template_name = 'users/register.html'