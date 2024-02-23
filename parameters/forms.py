from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Parameter


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ParametersForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ['compID', 'parameter1', 'parameter2', 'parameter3', 'parameter4']
        widgets = {
            'compID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write compID'}),
            'parameter1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 1'}),
            'parameter2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 2'}),
            'parameter3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 3'}),
            'parameter4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 4'}),
        }
