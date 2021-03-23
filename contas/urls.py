from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # HOME
    path('', views.index, name='index'),
    path('transacao/<int:pk>', views.transacao, name='transacao'),
    path('detalhe-transacao/<int:pk>', views.detalhe_transacao, name='detalhe-transacao'),
    path('new/', views.new, name='new'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete')
]