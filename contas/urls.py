from django.urls import path
from django.contrib import admin
from .views import index, transacao, detalhe_transacao, delete, update, new, register_category

urlpatterns = [
    #HOME
    path('', index, name='index'),
    
    #CADASTRAR
    path('new/', new, name='new'),
    path('register-category', register_category, name="register_category"),
    
    #VISUALIZAR
    path('detalhe-transacao/<int:pk>', detalhe_transacao, name='detalhe-transacao'),
    path('transacao/<int:pk>', transacao, name='transacao'),
    
    #ATUALIZAR
    path('update/<int:pk>', update, name='update'),
    
    #DELETAR
    path('delete/<int:pk>', delete, name='delete')
]