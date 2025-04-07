from ninja import Router
from .schemas import *
from .models import *
from ninja.errors import HttpError
from django.db import IntegrityError
from typing import List

rota_router = Router()

@rota_router.post('/motorista/', response={200: MotoristaSchema})
def criar_motorista(request, motorista_schema: MotoristaSchema):
    if Motorista.objects.filter(email=motorista_schema.email).exists():
        raise HttpError(400, "Email já cadastrado")

    motorista = Motorista.objects.create(**motorista_schema.dict())
    return motorista

@rota_router.put('/motorista/{motorista_id}/', response={200: MotoristaSchema})
def atualizar_motorista(request, motorista_id: int, motorista_schema: MotoristaSchema):
    try:
        motorista = Motorista.objects.get(id=motorista_id)

        # Verifica se o email foi alterado e se já existe
        if motorista.email != motorista_schema.email:
            if Motorista.objects.filter(email=motorista_schema.email).exclude(id=motorista_id).exists():
                raise HttpError(400, "Email já cadastrado por outro motorista")

        # Atualiza todos os campos
        for field, value in motorista_schema.dict().items():
            setattr(motorista, field, value)

        motorista.save()
        return motorista

    except Motorista.DoesNotExist:
        raise HttpError(404, "Motorista não encontrado")
    except IntegrityError:
        raise HttpError(400, "Erro de integridade no banco de dados")





@rota_router.get('/motorista/', response=List[MotoristaSchema])
def listar_motoristas(request):
    motoristas = Motorista.objects.all()
    return motoristas

@rota_router.delete('/motorista/{motorista_id}/', response={200: dict})
def deletar_motorista(request, motorista_id: int):
    try:
        motorista = Motorista.objects.get(id=motorista_id)
        motorista.delete()
        return {"message": "Motorista deletado com sucesso"}
    except Motorista.DoesNotExist:
        raise HttpError(404, "Motorista não encontrado")

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

@rota_router.put('/aluno/{aluno_id}/', response={200: AlunosSchema})
def atualizar_aluno(request, aluno_id: int, aluno_schema: AlunosSchema):
    try:
        aluno = Alunos.objects.get(id=aluno_id)
        
        # Atualiza cada campo
        for field, value in aluno_schema.dict().items():
            setattr(aluno, field, value)
            
        aluno.save()
        return aluno
    except Alunos.DoesNotExist:
        raise HttpError(404, "Aluno não encontrado")
    except IntegrityError:
        raise HttpError(400, "Email já cadastrado por outro aluno")

@rota_router.delete('/aluno/{aluno_id}/', response={200: dict}) 
def deletar_aluno(request, aluno_id: int):
    try:
        aluno = Alunos.objects.get(id=aluno_id)
        aluno.delete()
        return {"message": "Aluno deletado com sucesso"}
    except Alunos.DoesNotExist:
        raise HttpError(404, "Aluno não encontrado")

@rota_router.post('/veiculo/', response={200: VeiculoSchema})
def criar_veiculo(request, payload: VeiculoSchema):
    
    if Veiculo.objects.filter(placa=payload.placa).exists():
        raise HttpError(400, "Placa já cadastrada")
    veiculo = Veiculo.objects.create(**payload.dict())
    return veiculo

@rota_router.get('/veiculos/', response=list[VeiculoSchema])
def listar_veiculos(request):
    return Veiculo.objects.all()

@rota_router.delete('/veiculo/{veiculo_id}/', response={200: dict})   
def deletar_veiculo(request, veiculo_id: int):
    try:
        veiculo = Veiculo.objects.get(id=veiculo_id)
        veiculo.delete()
        return {"message": "Veículo deletado com sucesso"}
    except Veiculo.DoesNotExist:
        raise HttpError(404, "Veículo não encontrado")

@rota_router.post('/rotas/', response={200: RotaSchema})
def criar_rota(request, payload: RotaSchema):
    rota = Rota.objects.create(**payload.dict())
    return rota

@rota_router.get('/rotas/', response=list[RotaSchema])
def listar_rotas(request):
    return Rota.objects.all()

@rota_router.delete('/rota/{rota_id}/', response={200: dict})
def deletar_rota(request, rota_id: int):
    try:
        rota = Rota.objects.get(id=rota_id)
        rota.delete()
        return {"message": "Rota deletada com sucesso"}
    except Rota.DoesNotExist:
        raise HttpError(404, "Rota não encontrada")

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






    

    