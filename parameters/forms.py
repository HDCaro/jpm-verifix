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
        fields = ['compID', 'product', 'value_date', 'security', 'notional', 'currency_pair', 'side']
        widgets = {
            'compID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write compID'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'value_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'security': forms.Select(attrs={'class': 'form-control'}),
            'notional': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter notional amount'}),
            'currency_pair': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter currency pair'}),
            'side': forms.Select(attrs={'class': 'form-control'}),
        }
