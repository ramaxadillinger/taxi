from django.contrib.auth import forms
from django.db import models
from .models import Trip, UserLogin
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
#         attrs={'class': 'form-control'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
#         attrs={'class': 'form-control'}))


class UserLoginForm(AuthenticationForm):
    model = UserLogin
    fields = ["username", "password"]
    widgets = {
        'username': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ввести имя пользователя'
        }),
        'password': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ввести пароль'
        })
    }


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ["phone", "destination"]
        widgets = {
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввести номер телефона'
            }),
            'destination': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввести пункт назначения'
            })
        }

