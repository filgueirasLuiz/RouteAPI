from ninja import ModelSchema
from ninja import Schema
from .models import *
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

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
        fields = ['id','placa', 'modelo', 'ano', 'capacidade', 'tipo', 'status', 'motorista']

class RotaSchema(ModelSchema):
    class Meta:
        model = Rota
        fields = ['id','nome', 'ponto_partida', 'ponto_destino', 'horario_saida', 'horario_chegada']

class AlunoSchema(Schema):
    id: int
    nome: str

class RotaSchema(Schema):
    id: int
    nome: str

class ConfirmacaoSchema(Schema):
    id: int
    aluno: AlunoSchema
    rota: RotaSchema
    confirmada: bool
    data_confirmacao: datetime
    observacao: Optional[str] = None

class ConfirmacaoInputSchema(Schema):
    observacao: Optional[str] = None