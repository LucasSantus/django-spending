from django.shortcuts import render
from contas.models import Category

def index(request):
    category = Category.objects.all()

    context = {
        'categorys': category,
    }

    return render(request, 'home/index.html', context)
