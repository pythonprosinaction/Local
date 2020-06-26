from django.urls import path

from . import views

urlpatterns = [
    path('webapp', views.index, name='index'),
    path('home', views.homepage, name='homepage'),
    path('about', views.about),
    path('', views.index, name='index')
]
