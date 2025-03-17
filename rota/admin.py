from django.contrib import admin
from .models import *

@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "ponto_partida","ponto_destino", "horario_saida", "horario_chegada")
    search_fields = ["nome"]

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf", "cnh", "telefone", "email", "data_nascimento", "data_cadastro", "data_atualizacao")
    search_fields = ["nome"]

@admin.register(Alunos)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "matricula", "endereco", "cpf", "data_nascimento", "telefone", "email", "instituicao")
    search_fields = ["nome", "matricula"]

@admin.register(Confirmacao)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "rota", "data_confirmacao", "confirmada", "observacao")
    list_filter = ["rota"]

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("id", "placa", "modelo", "ano", "capacidade", "tipo", "status", "motorista")
    list_filter = ("tipo", "status")
    search_fields = ["placa", "modelo"]
