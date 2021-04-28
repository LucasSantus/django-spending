from django.urls import path
from django.contrib import admin
from .views import index

urlpatterns = [
    #HOME
    path('', index, name='index'),
]