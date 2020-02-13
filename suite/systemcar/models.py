from django.conf import settings
from django.db import models
from django.utils import timezone

class Configuracoes(models.Model):
    Nome = models.CharField(max_length=200)
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

class Cliente(models.Model):
    Nome = models.CharField(max_length=200)
    Usuario = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Senha = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Nome

class Colaborador(models.Model):
    Nome = models.CharField(max_length=200)
    Usuario = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Senha = models.CharField(max_length=200)

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