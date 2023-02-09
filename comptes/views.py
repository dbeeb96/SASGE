from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


# Create your views here.

def loginPage(request):
    # le formulate de connexion
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, email=email, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
    context = {'form': form}
    return render(request, 'comptes/login.html', context)
