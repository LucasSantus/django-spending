from django.db import models

class Category(models.Model):
    name = models.CharField(
        verbose_name = "Título", 
        max_length=155,
    )
    
    description = models.TextField(
        verbose_name = "Descrição",
        null=True,
    )
    
    date_generated = models.DateTimeField(
        verbose_name = "Data da Criação", 
        auto_now=True,
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
        
class Transaction(models.Model):
    name = models.CharField(
        verbose_name = "Título",
        max_length=155,
    )
    
    description = models.TextField(
        verbose_name = "Descrição",
        null=True,
    )
    
    hour_generated = models.DateTimeField(
        verbose_name = "Data da Transação",
    )
    
    value = models.DecimalField(
        verbose_name = "Valor da Transação", 
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

    def __str__(self):
        return self.name