from django.urls import path
from comptes import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
]