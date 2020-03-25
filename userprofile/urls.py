from django.urls import path
from . import views
from userprofile.views import SignupView
#from users import views as user_views

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
]