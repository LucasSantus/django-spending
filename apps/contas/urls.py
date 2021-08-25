from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    # CATEGORY
    path('category/register/', register_category, name="register_category"),
    path('category/<int:id_category>/update/', update_category, name='update_category'),
    path('category/<int:id_category>/delete/', delete_category, name='delete_category'),

    # TRANSACTION
    path('transaction/<int:id_category>/register/', register_transaction, name='register_transaction'),
    path('transaction/<int:id_category>/list/', list_transaction, name='list_transaction'),
    path('transaction/<int:id_transaction>/detail/', detail_transaction, name='detail_transaction'),
    path('transaction/<int:id_transaction>/update/', update_transaction, name='update_transaction'),
    path('transaction/<int:id_transaction>/delete/', delete_transaction, name='delete_transaction'),
]