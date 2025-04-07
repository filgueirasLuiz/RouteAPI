from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Alunos(models.Model):
    # colocar foto 
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=11)
    instituicao = models.CharField(max_length=200)
    #data_cadastro = models.DateField(auto_now_add=True)
    #data_atualizacao = models.DateField(auto_now=True) 

    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    TIPO_CHOICES = [
        ('onibus', 'Ônibus'),
        ('van', 'Van'),
        ('micro', 'Micro-ônibus'),
    ]
    
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('manutencao', 'Em Manutenção'),
        ('inativo', 'Inativo'),
    ]
    
    placa = models.CharField(max_length=10, unique=True)  # Ex: "ABC1D23"
    modelo = models.CharField(max_length=50)  # Ex: "Mercedes-Benz OF-1721"
    ano = models.IntegerField()  # Ex: 2020
    capacidade = models.IntegerField()  # Número de passageiros
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True, blank=True, related_name='veiculos'
    )
    
    def __str__(self):
        return f"{self.modelo} ({self.placa})"
    
class Rota(models.Model):
    nome = models.CharField(max_length=100)  # Ex: "Rota Centro - Campus A"
    ponto_partida = models.CharField(max_length=100)  # Ex: "Prefeitura Municipal"
    ponto_destino = models.CharField(max_length=100)  # Ex: "Universidade XYZ"
    horario_saida = models.TimeField()  # Ex: "07:00"
    horario_chegada = models.TimeField()  # Ex: "08:30"
    
    def __str__(self):
        return self.nome 
    
    #--------------- ATUALIZAÇÃO -----------------------

class Confirmacao(models.Model): 
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    confirmada = models.BooleanField(default=False)  # Para registrar a presença
    data_confirmacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.rota.nome} ({'Confirmado' if self.confirmada else 'Não Confirmado'})"
