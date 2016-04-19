from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from game.models import Character, Room

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("login ou mot de passe invalide")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class NewCharacterFrom(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=50)
    avatar = forms.ImageField()
