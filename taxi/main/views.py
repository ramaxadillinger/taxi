from importlib import import_module

from django.shortcuts import render, redirect
from .models import Trip, UserLogin
from .forms import TripForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login, logout



def index(request):
    trips = Trip.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'main page', 'trips': trips})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Некорректные данные'
    form = TripForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)



def user_login(request):
    error = ''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create')
        else:
            error = 'Некорректные данные'

    form = UserLoginForm()
    context = {
            'form': form,
            'error': error
        }
    return render(request, 'main/login.html', context)

