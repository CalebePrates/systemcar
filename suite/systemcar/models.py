from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from systemcar import lista_opcoes
from simple_history.models import HistoricalRecords
from model_utils import FieldTracker

class TiposUsuarios(models.Model):
    Nome = models.CharField(max_length=60, db_index=True, null=True, blank=True)
    PermissaoUsuario = models.IntegerField(choices=lista_opcoes.OPCOES_PERMISSAO)

    def __str__(self):
        return str(self.Nome)

class UserManager(AbstractUser):
    TiposUsuarios = models.IntegerField(choices=lista_opcoes.OPCOES_COLABORADOR, null=True, blank=True)
    history = HistoricalRecords()
    tracker = FieldTracker()

class Estado(models.Model):
    Estado = models.CharField(max_length=30, null=True, blank=True, db_index=True)
    Sigla = models.CharField(max_length=5, db_index=True)
    def __str__(self):
        return self.Sigla

class Cidade(models.Model):
    Nome = models.CharField(max_length=100, db_index=True)
    NomeNormalizado = models.CharField(max_length=100, db_index=True,default='')
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, db_index=True, related_name='Cidade_Estado')
    def __str__(self):
        return self.Nome

class Bairro(models.Model):
    Nome = models.CharField(max_length=100, db_index=True)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, db_index=True, related_name='Bairro_Cidade')
    def __str__(self):
        return self.Nome

class Endereco(models.Model):
    CEP = models.DecimalField(max_digits=8, decimal_places=0, null=True, db_index=True)
    Bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, db_index=True, null=True, blank=True, related_name='Endereco_Bairro')
    Logradouro = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    Numero = models.IntegerField(null=True, blank=True)
    Latitude = models.DecimalField(max_digits=11, decimal_places=7, null=True, blank=True, db_index=True)
    Longitude = models.DecimalField(max_digits=11, decimal_places=7, null=True, blank=True, db_index=True)
    Complemento = models.CharField(max_length=75, null=True, blank=True, default='')

    def get_latitude(self):
        return str(self.Latitude).replace(',','.')

    def get_longitude(self):
        return str(self.Longitude).replace(',','.')
        
    def get_endereco(self):
        if self.CEP:
            return self.Logradouro + ', ' + str(self.Numero) + ', ' + str(self.Bairro) + ' - ' + str(self.Bairro.Cidade)
        else:
            return str(self.Latitude) + ', ' + str(self.Longitude)

    def __str__(self):
        if self.CEP:
            return self.Logradouro
        else:
            return str(self.Latitude) + ', ' + str(self.Longitude)


class Colaborador(models.Model):
    Usuario = models.ForeignKey(UserManager, on_delete=models.CASCADE, null=True, blank=True, related_name='Colaborador_UserManager', db_index=True)
    CriadoPor = models.ForeignKey(UserManager, on_delete=models.SET_NULL, null=True, blank=True, related_name='Colaborador_CriadoPor')
    Nome = models.CharField(max_length=50, blank=True)
    Email = models.CharField(max_length=50, blank=True)
    Telefone = models.CharField(max_length=12, blank=True)
    Endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True, db_index=True, related_name='Colaborador_Endereco')
    SituacaoNaEmpresa = models.IntegerField(choices=lista_opcoes.SITUACAO_NA_EMPRESA, null=True, blank=True)
    FotoPerfil = models.ImageField(upload_to='images', blank=True)
    TipoUsuario = models.IntegerField(choices=lista_opcoes.OPCOES_COLABORADOR)
    history = HistoricalRecords()
    tracker = FieldTracker()

    def __str__(self):
        return self.Nome

class Cliente(models.Model):
    Nome = models.CharField(max_length=50)
    CriadoPor = models.ForeignKey(UserManager, on_delete=models.SET_NULL, null=True, blank=True, related_name='Cliente_CriadoPor')
    Email = models.CharField(max_length=50, blank=True)
    Telefone = models.CharField(max_length=12, blank=True)
    Cpf = models.CharField(max_length=11, blank=True)
    DataNascimento = models.DateField(auto_now=False, null=True, blank=True)
    Endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True, db_index=True, related_name='Cliente_Endereco')
    TipoCliente = models.IntegerField(choices=lista_opcoes.OPCOES_CLIENTE)
    history = HistoricalRecords()
    tracker = FieldTracker()
    
    def __str__(self):
        return self.Nome

class Integrador(models.Model):
    Nome = models.CharField(max_length=100)
    Token = models.CharField(max_length=1000,null=True,blank=True)
    ClienteId = models.CharField(max_length=500,null=True,blank=True)
    url = models.CharField(max_length=50, null=True, blank=True, default=None)
    ClientSecret = models.CharField(max_length=1000,null=True,blank=True) #Client Secret informado pela Olx
    Observacoes = models.TextField(null=True, blank=True, default='') #Possível detalhe a mais do integrador
    AccountId = models.CharField(max_length=50,null=True,blank=True)
    Category = models.CharField(max_length=50,null=True,blank=True)
    GroupId = models.CharField(max_length=150,null=True,blank=True)
    Ativo = models.BooleanField(default=False)
    Icon = models.ImageField(upload_to='media/integradores', null=True, blank=True)
    def __str__(self):
        return self.Nome

    def save(self, *args, **kwargs):
        if self.Token:
            self.Ativo = True
        else:
            self.Ativo = False
        super(Integrador, self).save(*args, **kwargs)

    def get_page_name(self):
        if self.Observacoes:
            try:
                name = json.loads(self.Observacoes).get('name')
            except:
                name = json.loads(self.Observacoes.replace("'",'"')).get('name')

            return name
        return ''

class Configuracoes(models.Model):
    Nome = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=200)
    Celular = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome

class Automovel(models.Model):
    Nome = models.CharField(max_length=200)
    Marca = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    DataModificacao = models.DateTimeField()
    DataCriacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Nome

class Contrato(models.Model):
    Autor = models.CharField(max_length=200)

    def __str__(self):
        return self.Autor

class Atendimento(models.Model):
    Autor = models.CharField(max_length=200)

    def __str__(self):
        return self.Autor

class Contato(models.Model):
    Nome = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Telefone = models.CharField(max_length=200)
    ModoContato = models.CharField(max_length=200)
    Mensagem = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome

class Lead(models.Model):
    Nome = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Telefone = models.CharField(max_length=200)
    ModoContato = models.CharField(max_length=200)
    Mensagem = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome