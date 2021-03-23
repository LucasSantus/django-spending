from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # HOME
    path('', views.index, name='index'),
    path('categoria/<int:pk>', views.categoria, name='categoria'),
    path('new/', views.new, name='new'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete')
]