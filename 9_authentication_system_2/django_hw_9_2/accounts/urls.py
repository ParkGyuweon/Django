from django.urls import path
from .models import User
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('singup/', views.signup, name='signup'),
]
