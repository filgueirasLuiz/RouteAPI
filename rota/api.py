from ninja import Router
from .schemas import MotoristaSchema, AlunosSchema
from .models import Motorista, Alunos
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

@rota_router.post('/aluno/', response={200: AlunosSchema})
def criar_aluno(request, aluno_schema : AlunosSchema):
    data = aluno_schema.dict()
    nome = data['nome']
    endereco = data['endereco']
    cpf = data['cpf']
    data_nascimento = data['data_nascimento']
    telefone = data['telefone']
    email = data['email']
    matricula = data['matricula']
    instituicao = data['instituicao']

    if Alunos.objects.filter(email=email).exists():
        raise HttpError(400, "Email já cadastrado")

    aluno = Alunos(nome=nome,
                   endereco=endereco,
                   cpf=cpf,
                   data_nascimento=data_nascimento,
                   telefone=telefone,
                   email=email,
                   matricula=matricula,
                   instituicao=instituicao)
    aluno.save()

    return aluno
@rota_router.get('/alunos/', response=List[AlunosSchema])
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos