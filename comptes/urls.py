from django.urls import path
from comptes import views

app_name = 'register_app'

urlpatterns = [
    path('login/', views.loginPage, name="login"),
]
