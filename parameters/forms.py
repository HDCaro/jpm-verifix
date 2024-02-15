from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Parameter


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ParametersForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ['parameter1', 'parameter2', 'parameter3', 'parameter4', 'parameter5', 'user']
        widgets = {
            'parameter1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 1'}),
            'parameter2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 2'}),
            'parameter3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 3'}),
            'parameter4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 4'}),
            'parameter5': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write parameter 5'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
