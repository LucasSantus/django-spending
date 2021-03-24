from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(verbose_name = "Nome", max_length=100)
    dt_criacao = models.DateTimeField(verbose_name = "Data Criação", auto_now_add=True)

    def __str__(self):
        return self.nome
        
class Transacao(models.Model):
    nome = models.CharField(verbose_name = "Nome",max_length=194,)
    descricao = models.TextField(verbose_name = "Descrição",)
    data = models.DateTimeField(verbose_name = "Data",)
    valor = models.DecimalField(verbose_name = "Valor", max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
    
    def __str__(self):
        return self.descricao