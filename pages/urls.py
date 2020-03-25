from django.urls import path
from . import views
from pages.views import HomeView
#from users import views as user_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('register/', SignupView.as_view(), name='register'),
]