from django.shortcuts import render, redirect
from .models import *
from .form import *
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['row'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

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
