from django.urls import  path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'register_app'

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.SignupView, name="register"),
]
