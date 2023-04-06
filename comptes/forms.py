from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django import forms
from django.forms import EmailField, TextInput, PasswordInput, ImageField

from django.utils.translation import gettext_lazy as _  # for protected-


class LoginForm(AuthenticationForm):
    pass

    AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (

            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']
        user.email = self.cleaned_data['email']
        # user.company_name=self.cleaned_data['company_name']

        if commit:
            user.save()

        return user

