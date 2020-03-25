from django.shortcuts import render
from django.views.generic import TemplateView


# dashboard home views

class DashboardView(TemplateView):
    template_name ='dashboard/home.html'
