from django.shortcuts import render, redirect
from .models import *
from .form import *
import datetime

def index(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias,
        'data': datetime.datetime.now()
    }

    return render(request, 'contas/index.html', context)

def transacao(request, pk):
    categorias = Categoria.objects.filter(pk=pk)
    transacoes = Transacao.objects.filter(categoria = pk)
    
    context = {
        'categorias': categorias,
        'transacoes': transacoes,
    }
    return render(request, 'contas/transacao.html', context)

def detalhe_transacao(request, pk):
    categorias = Categoria.objects.filter(pk=pk)
    transacoes = Transacao.objects.filter(categoria = pk)
    
    context = {
        'categorias': categorias,
        'transacoes': transacoes,
    }
    return render(request, 'contas/transacao.html', context)


def new(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categoria')

    context = {
        'form': form,
    }

    return render(request, 'contas/form.html', context)

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
