from django.urls import path
from django.contrib import admin
from .views import register_category, register_transaction, list_transaction, detail_transaction, update_category, update_transaction, delete_category, delete_transaction

urlpatterns = [
    #CADASTRAR
    path('register-category/', register_category, name="register_category"),
    path('register-transaction/<int:id_category>/', register_transaction, name='register_transaction'),
    
    #VISUALIZAR
    path('list-transaction/<int:id_category>/', list_transaction, name='list_transaction'),
    path('detail-transaction/<int:id_transaction>/', detail_transaction, name='detail_transaction'),
    
    #ATUALIZAR
    path('update-category/<int:id_category>/', update_category, name='update_category'),
    path('update-transaction/<int:id_transaction>/', update_transaction, name='update_transaction'),
    
    #DELETAR
    path('delete-category/<int:id_category>/', delete_category, name='delete_category'),
    path('delete-transaction/<int:id_transaction>/', delete_transaction, name='delete_transaction'),
]