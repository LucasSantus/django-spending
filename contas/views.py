from django.shortcuts import render
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
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return listagem(request)

    data['form'] = form
    return render(request, 'contas/form.html', data)