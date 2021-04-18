from django.shortcuts import render, redirect
from .models import *
from .form import *
import datetime

def index(request):
    category = Category.objects.all()

    context = {
        'categorys': category,
        'date': datetime.datetime.now()
    }

    return render(request, 'contas/index.html', context)

def register_category(request):

    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'contas/register-category.html', context)

def register_transaction(request):
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'contas/register-transaction.html', context)

def list_transaction(request, id_category):
    categorys = Category.objects.filter(pk=id_category)
    transactions = Transaction.objects.filter(category=id_category)
    
    context = {
        'categorys': categorys,
        'transactions': transactions,
    }
    
    return render(request, 'contas/list-transactions.html', context)

def detail_transaction(request, pk):
    
    categorys = Category.objects.filter(pk=id_category)
    transactions = Transaction.objects.filter(pk=pk, category = pk)
    
    context = {
        'categorys': categorys,
        'transactions': transactions,
    }
    return render(request, 'contas/detail-transaction.html', context)

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('transacao')

    context = {
        'form': form,
        'transacao': transacao
    }

    return render(request, 'contas/form.html', context)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()

    return redirect('transacao')
