from django.urls import path
from django.contrib import admin
from .views import index, transacao, detalhe_transacao, delete, update, new, register_category

urlpatterns = [
    #HOME
    path('', index, name='index'),
    
    #CADASTRAR
    path('register-category/', register_category, name="register_category"),
    path('register-transaction/', register_transaction, name='register_transaction'),
    
    #VISUALIZAR
    path('list-transaction/<int:id_category>', list_transaction, name='list_transaction'),
    path('detail-transaction/<int:pk>', detail_transaction, name='detail_transaction'),
    
    #ATUALIZAR
    path('update-category/<int:id_category>', update_category, name='update_category'),
    path('update-transaction/<int:id_transaction>', update_transaction, name='update_transaction'),
    
    #DELETAR
    path('delete-category/<int:id_category>', delete_category, name='delete_category'),
    path('delete-transaction/<int:id_transaction>', delete_transaction, name='delete_transaction'),
]