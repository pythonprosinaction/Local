from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'webapp/home.html')


def about(request):
    return render(request, 'webapp/about.html')


def homepage(request):
    return render(request, 'webapp/home.html')


def dashboard(request):
    return render(request, 'webapp/dashboard.html')
