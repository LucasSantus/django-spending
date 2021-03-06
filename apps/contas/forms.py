from django.forms import ModelForm
from .models import Category, Transaction

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        
        error_messages = {
            "name":{
                "required": "Insira o Título da Categoria!",
            },
            "description":{
                "required": "Insira a Descrição da Categoria!",
            },
        }

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = ['category']
        
        error_messages = {
            "name":{
                "required": "Insira o Título da Transação!",
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
        }
