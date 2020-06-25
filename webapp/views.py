from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at index page of your application")


def homepage(request):
    return render(request, 'webapp/homepage.html')

