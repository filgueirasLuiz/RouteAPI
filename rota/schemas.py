from ninja import ModelSchema
from .models import Motorista

class MotoristaSchema(ModelSchema):
    class Meta:
        model = Motorista
        fields = ['nome', 'cpf', 'cnh', 'telefone', 'email', 'data_nascimento']
