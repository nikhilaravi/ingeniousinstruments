from django.core.context_processors import request
from django.shortcuts import render

__author__ = 'watsontom100'

def home(request):
    name = 'Tom'
    return render(request, 'home.html', {'name': name})


def about(request):
    return render(request, 'about.html')


def upload(request):
    return render(request, 'upload.html')

def investors(request):
    return render(request, 'investors.html')
