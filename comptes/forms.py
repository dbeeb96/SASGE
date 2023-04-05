from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django import forms
from django.forms import EmailField, TextInput, PasswordInput, ImageField

from django.utils.translation import ugettext_lazy as _  # for protected-


class LoginForm(AuthenticationForm):
    pass

    AuthenticationForm


CHOICES = (
    ('CEO', 'CEO'),
    ('Assistance', 'Assistance'),
    ('DESE', 'DESE'),
    ('DEF', 'DEF'),
    ('DIT', 'DIT'),
    ('SAIN', 'SAIN'),
    ('DICM', 'DICM' ),
    ('SLO', 'SLO'),
    ('DIP', 'DIP'),
)


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Entrer votre nom d'utilisateur :"})
                               , label='Nom d\'utilisateur')

    prenom = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Entrer votre nom :"})
                               , label=' Entrer votre prenom')

    nom = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Entrer votre nom :"})
                               , label=' Entrer votre nom')


    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Enter votre mot de passe : "}))

    password1 = forms.CharField \
        (widget=forms.TextInput(attrs={"placeholder": "Entrer votre mot de passe", 'type': 'password'}),
         label=_("Mot de passe"))

    password2 = forms.CharField \
        (widget=forms.TextInput(attrs={"placeholder": "Confirmer votre mot de passe", 'type': 'password'}),
         label=_("Confirmer le mot de passe"))

    users = forms.ChoiceField(choices=CHOICES, label='Directions')
    # La classe Meta

    class Meta:
        model = User
        fields = (

            'username',
            'prenom',
            'nom',
            'email',
            'password1',
            'password2',
            'users'
        )
        # Le help_text va supprimer le text par défaut dans la page d'inscription
        help_texts = {
            'username': None,
        }
