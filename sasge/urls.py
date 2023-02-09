from django.contrib import admin
from django.urls import include, path
from django.urls import include
from comptes import views
from comptes.views import loginPage

urlpatterns = [
    path('', include('base1.urls')),
    path('admin/', admin.site.urls),
    path('login/', loginPage, name='login')
]
