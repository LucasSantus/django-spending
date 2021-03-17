from django.shortcuts import render
import datetime
from .models import Transacao


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['row'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)