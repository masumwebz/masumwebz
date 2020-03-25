from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from django.urls import reverse_lazy
from .forms import SignUpForm


# dashboard home views

class DashboardView(TemplateView):
    template_name ='dashboard/home.html'




# signup view
class SignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('dashboard')
    template_name = 'dashboard/register.html'