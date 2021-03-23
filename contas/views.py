from django.shortcuts import render, redirect
from .models import *
from .form import *
import datetime

def home(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias,
        'data': datetime.datetime.now()
    }

    return render(request, 'contas/home.html', context)

def listagem(request, pk):
    categoria = Categoria.objects.filter(pk=pk)
    transacoes = Transacao.objects.filter(categoria = pk)
    
    context = {
        'categoria': categoria,
        'transacoes': transacoes,
    }
    return render(request, 'contas/listagem.html', context)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem')

    context = {
        'form': form,
    }

    return render(request, 'contas/form.html', context)

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('listagem')

    context = {
        'form': form,
        'transacao': transacao
    }

    return render(request, 'contas/form.html', context)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()

    return redirect('listagem')
