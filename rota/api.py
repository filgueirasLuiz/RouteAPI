from ninja import Router
from .schemas import MotoristaSchema
from .models import Motorista
from ninja.errors import HttpError
from typing import List

rota_router = Router()

@rota_router.post('', response={200: MotoristaSchema})
def criar_motorista(request, motorista_schema : MotoristaSchema):
    data = motorista_schema.dict()
    nome = data['nome']
    cpf = data['cpf']
    cnh = data['cnh']
    telefone = data['telefone']
    email = data['email']
    data_nascimento = data['data_nascimento']

    if Motorista.objects.filter(email=email).exists():
        raise HttpError(400 , "Email já cadastrado")

    motorista = Motorista(nome=nome, 
                          cpf=cpf, 
                          cnh=cnh, 
                          telefone=telefone, 
                          email=email, 
                          data_nascimento=data_nascimento)
    motorista.save()

    return motorista

@rota_router.get('/motorista/', response=List[MotoristaSchema])
def listar_motoristas(request):
    motoristas = Motorista.objects.all()
    return motoristas