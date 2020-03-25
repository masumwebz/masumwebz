from django.urls import path
from . import views
from dashboard.views import DashboardView, SignupView
#from users import views as user_views

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

]