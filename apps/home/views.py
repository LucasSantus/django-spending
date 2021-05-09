from django.shortcuts import render
from contas.models import Category
from datetime import date

def index(request):
    category = Category.objects.all()

    context = {
        'categorys': category,
    }

    return render(request, 'home/index.html', context)

def base(request):
    context = { 
    	'date': date.today()
    }
    return context