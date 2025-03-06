from ninja import ModelSchema
from .models import Motorista, Alunos, Veiculo, Rota
from datetime import datetime

class MotoristaSchema(ModelSchema):
    class Meta:
        model = Motorista
        fields = ['nome', 'cpf', 'cnh', 'telefone', 'email', 'data_nascimento']

class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'endereco', 'cpf', 'data_nascimento', 'telefone', 'email', 'matricula', 'instituicao']

class VeiculoSchema(ModelSchema):
    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo', 'ano', 'capacidade', 'tipo', 'status', 'motorista']

class RotaSchema(ModelSchema):
    class Meta:
        model = Rota
        fields = ['nome', 'ponto_partida', 'ponto_destino', 'horario_saida', 'horario_chegada']

