from ninja import ModelSchema
from .models import Motorista, Alunos

class MotoristaSchema(ModelSchema):
    class Meta:
        model = Motorista
        fields = ['nome', 'cpf', 'cnh', 'telefone', 'email', 'data_nascimento']

class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'endereco', 'cpf', 'data_nascimento', 'telefone', 'email', 'matricula', 'instituicao']