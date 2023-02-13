from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django import forms
from django.forms import EmailField, TextInput, PasswordInput, ImageField

from django.utils.translation import ugettext_lazy as _  # for protected-


class LoginForm(AuthenticationForm):
    pass

    AuthenticationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Entrer votre nom d'utilisateur :"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Enter votre mot de passe : "}))
    password1 = forms.CharField \
        (widget=forms.TextInput(attrs={"placeholder": "Entrer votre mot de passe", 'type': 'password'}),
         label=_("Password"))
    password2 = forms.CharField \
        (widget=forms.TextInput(attrs={"placeholder": "Confirmer votre mot de passe", 'type': 'password'}),
         label=_("Confirm Password"))

    # La classe Meta

    class Meta:
        model = User
        fields = (

                  'username',
                  'email',
                  'password1',
                  'password2',

                  )
        # Le help_text va supprimer le text par défaut dans la page d'inscription
        help_texts = {
            'username': None,
        }
