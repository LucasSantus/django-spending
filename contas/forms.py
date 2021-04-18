from django.forms import ModelForm
from .models import Categoria, Transacao

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        
        error_messages = {
            "nome":{
                "required": "É obrigatório o Nome Completo do individuo para a realização do registro",
            },
        }


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['nome','descricao','data','valor','categoria']
        
        error_messages = {
            "nome":{
                "required": "É obrigatório o Nome Completo do individuo para a realização do registro",
            },

            "cpf":{
                "required": "É obrigatório o CPF do individuo para a realização do registro",
                "invalid": "Insira um CPF válido!",
            },
            "data_nascimento":{
                "required": "É obrigatório a Data de Nascimento do individuo para a realização do registro",
                "invalid": "Insira uma Data de Nascimento válida!",
            },
            "password":{
                "required": "É obrigatório a Senha do individuo para a realização do registro",
            },
        }
