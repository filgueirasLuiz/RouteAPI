from ninja import Router
from .schemas import *
from .models import *
from ninja.errors import HttpError
from typing import List

rota_router = Router()

@rota_router.post('', response={200: MotoristaSchema})
def criar_motorista(request, motorista_schema: MotoristaSchema):
    if Motorista.objects.filter(email=motorista_schema.email).exists():
        raise HttpError(400, "Email já cadastrado")

    motorista = Motorista.objects.create(**motorista_schema.dict())
    return motorista

@rota_router.get('/motorista/', response=List[MotoristaSchema])
def listar_motoristas(request):
    motoristas = Motorista.objects.all()
    return motoristas

@rota_router.post('/aluno/', response={200: AlunosSchema})
def criar_aluno(request, aluno_schema: AlunosSchema):
    if Alunos.objects.filter(email=aluno_schema.email).exists():
        raise HttpError(400, "Email já cadastrado")

    aluno = Alunos.objects.create(**aluno_schema.dict())
    return aluno

@rota_router.get('/alunos/', response=List[AlunosSchema])
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos

@rota_router.post('/veiculo/', response={200: VeiculoSchema})
def criar_veiculo(request, payload: VeiculoSchema):
    
    if Veiculo.objects.filter(placa=payload.placa).exists():
        raise HttpError(400, "Placa já cadastrada")
    veiculo = Veiculo.objects.create(**payload.dict())
    return veiculo

@rota_router.get('/veiculos/', response=list[VeiculoSchema])
def listar_veiculos(request):
    return Veiculo.objects.all()

@rota_router.post('/rotas/', response={200: RotaSchema})
def criar_rota(request, payload: RotaSchema):
    rota = Rota.objects.create(**payload.dict())
    return rota

@rota_router.get('/rotas/', response=list[RotaSchema])
def listar_rotas(request):
    return Rota.objects.all()

@rota_router.post('/confirmar-presenca/{aluno_id}/{rota_id}/', response={200: ConfirmacaoSchema})
def confirmar_presenca(request, aluno_id: int, rota_id: int, dados: ConfirmacaoInputSchema):
    try:
        aluno = Alunos.objects.get(id=aluno_id)
        rota = Rota.objects.get(id=rota_id)
        
        # Verifica se já existe uma confirmação para este aluno e esta rota
        if Confirmacao.objects.filter(aluno=aluno, rota=rota).exists():
            raise HttpError(400, "Presença já confirmada para esta rota")

        # Cria a confirmação de presença
        confirmacao = Confirmacao.objects.create(aluno=aluno, rota=rota, observacao=dados.observacao)

        return confirmacao  # Retorna os dados do modelo ConfirmacaoSchema
    except Alunos.DoesNotExist:
        raise HttpError(404, "Aluno não encontrado")
    except Rota.DoesNotExist:
        raise HttpError(404, "Rota não encontrada")
    except Exception as e:
        raise HttpError(500, f"Erro interno: {str(e)}")  # Captura outros erros

    
@rota_router.get('/confirmacoes/', response=list[ConfirmacaoSchema])
def listar_confirmacoes(request):
    confirmacoes = Confirmacao.objects.all()
    return confirmacoes

@rota_router.delete('/confirmar-presenca/{confirmacao_id}/', response={200: dict})
def deletar_confirmacao(request, confirmacao_id: int):
    try:
        confirmacao = Confirmacao.objects.get(id=confirmacao_id)
        confirmacao.delete()
        return {"message": "Confirmação deletada com sucesso"}
    except Confirmacao.DoesNotExist:
        raise HttpError(404, "Confirmação não encontrada")
