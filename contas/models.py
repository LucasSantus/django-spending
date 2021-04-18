from django.db import models

class Category(models.Model):
    name = models.CharField(
        verbose_name = "Nome da Categoria: ", 
        max_length=155,
    )
    
    description = models.TextField(
        verbose_name = "Descrição da Categoria: ",
        max_length=300,
    )
    
    date_generated = models.DateTimeField(
        verbose_name = "Data da Criação: ", 
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "category"

    def __str__(self):
        return self.nome
        
class Transaction(models.Model):
    name = models.CharField(
        verbose_name = "Nome da Transação: ",
        max_length=155,
    )
    
    description = models.TextField(
        verbose_name = "Descrição da Transação: ",
        max_length=300,
    )
    
    date = models.DateTimeField(
        verbose_name = "Data da Transação: ",
    )
    
    value = models.DecimalField(
        verbose_name = "Valor da Transação: ", 
        max_digits=7, 
        decimal_places=2,
    )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
        db_table = "transaction"

    def __str__(self):
        return self.nome