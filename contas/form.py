from django.forms import ModelForm
from .models import *

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['nome','descricao','data','valor','categoria']