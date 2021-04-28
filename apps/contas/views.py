from django.shortcuts import render, redirect
from .models import Category, Transaction
from .forms import CategoryForm, TransactionForm
import datetime

def index(request):
    category = Category.objects.all()

    context = {
        'categorys': category,
        'date': datetime.datetime.now()
    }

    return render(request, 'contas/index.html', context)

def register_category(request):
    
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'name_page': "Categoria",
        'form': form,
    }

    return render(request, 'contas/register-category.html', context)

def register_transaction(request, id_category):
    category = Category.objects.get(pk=id_category)
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.category = category
            transacao.save()
            return redirect('list_transaction', id_category)

    context = {
        'name_page': "Transação",
        'form': form,
        'category': category,
    }

    return render(request, 'contas/register-transaction.html', context)

def list_transaction(request, id_category):
    categorys = Category.objects.filter(id=id_category)
    transactions = Transaction.objects.filter(category=id_category)
    
    context = {
        'categorys': categorys,
        'transactions': transactions,
    }
    
    return render(request, 'contas/list-transactions.html', context)

def detail_transaction(request, id_transaction):
    
    transactions = Transaction.objects.filter(pk=id_transaction)
    
    context = {
        'transactions': transactions,
    }
    return render(request, 'contas/detail-transaction.html', context)

def update_category(request, id_category):
    category = Category.objects.get(pk=id_category)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'name_page': "Editar Categoria",
        'name_button': "EDITAR",
        'form': form,
        'category': category,
    }

    return render(request, 'contas/register-category.html', context)

def update_transaction(request, id_transaction):
    transaction = Transaction.objects.get(pk=id_transaction)
    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'transaction': transaction,
    }

    return render(request, 'contas/register-transaction.html', context)

def delete_category(request, id_category):
    category = Category.objects.get(pk=id_category)
    category.delete()

    return redirect('index')

def delete_transaction(request, id_transaction):
    transaction = Transaction.objects.get(pk=id_transaction)
    transaction.delete()

    return redirect('index')
