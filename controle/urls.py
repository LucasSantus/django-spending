from django.contrib import admin
from django.urls import path, include
from contas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contas.urls')),
]
