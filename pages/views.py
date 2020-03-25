from django.shortcuts import render
from django.views.generic import TemplateView




# dashboard home views

class HomeView(TemplateView):
    template_name ='homepage/blog.html'
