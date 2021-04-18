from django.forms import ModelForm
from .models import Category, Transaction

class CategoryForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']
        
        error_messages = {
            "name":{
                "required": "Insira o Nome da Categoria!",
            },
        }

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['__all__']
        
        error_messages = {
            "name":{
                "required": "Insira o Nome da Transação!",
            },

            "description":{
                "required": "Insira a Descrição da Transação!",
                "invalid": "Insira um CPF válido!",
            },
            
            "date":{
                "required": "Insira a Data da Transação!",
                "invalid": "Insira uma Data válida!",
            },
            
            "value":{
                "required": "Insira o Valor da Transação!",
            },
            
            "category":{
                "required": "Insira uma Categoria para a Transação!",
            },
        }
