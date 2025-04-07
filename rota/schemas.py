from ninja import ModelSchema
from ninja import Schema
from .models import *
from datetime import datetime

class MotoristaSchema(ModelSchema):
    class Meta:
        model = Motorista
        fields = ['id','nome', 'cpf', 'cnh', 'telefone', 'email', 'data_nascimento']

class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['id','nome', 'endereco', 'cpf', 'data_nascimento', 'telefone', 'email', 'matricula', 'instituicao']

class VeiculoSchema(ModelSchema):
    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo', 'ano', 'capacidade', 'tipo', 'status', 'motorista']

class RotaSchema(ModelSchema):
    class Meta:
        model = Rota
        fields = ['nome', 'ponto_partida', 'ponto_destino', 'horario_saida', 'horario_chegada']

class ConfirmacaoSchema(ModelSchema):
    class Meta:
        model = Confirmacao
        fields = ['aluno', 'rota','confirmada', 'data_confirmacao', 'observacao']  

class ConfirmacaoInputSchema(Schema):
    observacao: str = None