from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome