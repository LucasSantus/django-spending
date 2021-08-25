from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    # CATEGORY
    path('category/register/', register_category, name="register_category"),
    path('category/update/<int:id_category>/', update_category, name='update_category'),
    path('category/delete/<int:id_category>/', delete_category, name='delete_category'),

    # TRANSACTION
    path('transaction/register/<int:id_category>/', register_transaction, name='register_transaction'),
    path('transaction/list/<int:id_category>/', list_transaction, name='list_transaction'),
    path('transaction/detail/<int:id_transaction>/', detail_transaction, name='detail_transaction'),
    path('transaction/update/<int:id_transaction>/', update_transaction, name='update_transaction'),
    path('transaction/delete/<int:id_transaction>/', delete_transaction, name='delete_transaction'),
]