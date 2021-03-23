from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),
    path('listagem/<int:pk>', views.listagem, name='listagem'),
    path('nova/', views.nova_transacao, name='nova_transacao'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete')
]