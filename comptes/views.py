from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm # ,UpdateDefaultProfile,UpdateCustomProfile


# Create your views here.

def loginPage(request):
    # le formulate de connexion
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        prenom = request.POST.geet('prenom')
        nom = request.POST.get('nom')
        password = request.POST.get('password')
        email = request.POST.get('email')
        users = request.POST.get('users')

        user = authenticate(request, email=email, username=username, prenom=prenom,  nom=nom, password=password, users=users)
        if user is not None:
            login(request, user)
            return redirect('base1')

    context = {'form': form}
    return render(request, 'comptes/login.html', context)


# formulaire d'inscription


def SignupView(request):
    form = SignupForm()

    context = {'form': form}
    return render(request, 'comptes/register.html', context)
