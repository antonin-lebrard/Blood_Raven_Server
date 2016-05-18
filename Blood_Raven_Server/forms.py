from django.contrib.auth.models import User
from django.forms import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': (''),
            'password': (''),
        }
        help_texts = {
            'username': ('\n'),
            'password': ('\n'),
        }
        widgets = {'username': TextInput(attrs={'placeholder': "Nom d'utilisateur"}), 'password': PasswordInput(attrs={'placeholder': 'Mot de passe'}) }
