from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import redirect
from .views_admin import *
from datetime import datetime
from django.conf import settings
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

@permission_classes((IsAuthenticated,))
class cadastrar_colaborador_rest(APIView):
    """
    Função responsável por cadastrar um colaborador no sistema
    """
    def get(self, request):
        raise exceptions.MethodNotAllowed()

    def post(self, request, *args, **kwargs):
        try:
            colaborador = None
            existColaborador = None
            if request.POST.get('idColaborador'):
                existColaborador = Colaborador.objects.filter(id=request.POST.get('idColaborador')).first()
            if existColaborador:
                colaborador = existColaborador
            else:
                if request.POST.get('usuarioColaborador') and request.POST.get('senhaColaborador') and len(request.POST.get('senhaColaborador')) > 3:
                    usuario = UserManager.objects.create_user(username=str(request.POST.get('usuarioColaborador')),password=str(request.POST.get('senhaColaborador')))
                    usuario.save()
                    colaborador = Colaborador()
                    colaborador.Usuario = usuario
                    colaborador.CriadoPor = request.user
                else:
                    return JsonResponse({'msg': 'Não existe um usuário com as informações passadas ou não foi passado o usuario e senha para a função.'}, status=400)

            # Email e Telefone podem ser retirados das informações do colaborador caso necessário, por isso não existe tratativas
            colaborador.Email = str(request.POST.get('emailColaborador'))
            colaborador.Telefone = str(request.POST.get('telefoneColaborador'))

            if request.POST.get('nomeColaborador'):
                colaborador.Nome = str(request.POST.get('nomeColaborador'))
            if request.POST.get('situacaoColaborador'):
                colaborador.SituacaoNaEmpresa = int(request.POST.get('situacaoColaborador'))
            if request.POST.get('tipoColaborador'):
                colaborador.TipoUsuario = str(request.POST.get('tipoColaborador'))
            if request.POST.get('enderecoColaborador'):
                if colaborador.Endereco:
                    colaborador.Endereco = setEndereco(colaborador.Endereco, request, 'Colaborador')
                else:
                    newEndereco = Endereco()
                    colaborador.Endereco = setEndereco(newEndereco, request, 'Colaborador')

            colaborador.save()

            if colaborador.Email and not existColaborador:
                msg = MIMEMultipart()

                # setup the parameters of the message
                msg['From'] = settings.EMAIL_EMAIL_CLIENTE
                msg['To'] = colaborador.Email
                msg['Subject'] = "Bem-vindo! Aqui estão seus dados"

                mensagem = "Nome:" + str(colaborador.Nome) + "\nUsuário:" + str(request.POST.get('usuarioColaborador')) + "\nSenha:" + str(request.POST.get('senhaColaborador'))
                # create server
                msg.attach(MIMEText(mensagem, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com: 587')
                
                server.starttls()
                
                # Login Credentials for sending the mail
                server.login(settings.EMAIL_EMAIL_CLIENTE, settings.PASSWORD_EMAIL_CLIENTE)
                
                
                # send the message via the server.
                server.sendmail(settings.EMAIL_EMAIL_CLIENTE, colaborador.Email, msg.as_string())
                
                server.quit()

            return JsonResponse({'msg': 'Colaborador cadastrado com sucesso!'}, status=200)

        except Exception as e:
            raise exceptions.ParseError({'msg': 'Erro ao processar o request', 'ex': str(e)})

    def initial(self, request, *args, **kwargs):
        super(cadastrar_colaborador_rest, self).initial(request, *args, **kwargs)

@permission_classes((IsAuthenticated,))
class cadastrar_cliente_rest(APIView):
    """
    Função responsável por cadastrar um cliente no sistema
    """
    def get(self, request):
        raise exceptions.MethodNotAllowed()

    def post(self, request, *args, **kwargs):
        try:
            cliente = None
            existCliente = None
            if request.POST.get('idCliente'):
                existCliente = Cliente.objects.filter(id=request.POST.get('idCliente')).first()
            if existCliente:
                cliente = existCliente
            else:
                cliente = Cliente()
                cliente.CriadoPor = request.user

            # Email e Telefone podem ser retirados das informações do cliente caso necessário, por isso não existe tratativas
            cliente.Email = str(request.POST.get('emailCliente'))
            cliente.Telefone = str(request.POST.get('telefoneCliente'))

            if request.POST.get('nomeCliente'):
                cliente.Nome = str(request.POST.get('nomeCliente'))
            if request.POST.get('cpfCliente'):
                cliente.Cpf = str(request.POST.get('cpfCliente'))
            if request.POST.get('dataNascimentoCliente'):
                cliente.DataNascimento = datetime.strptime(request.POST.get('dataNascimentoCliente'), '%d/%m/%Y')
            if request.POST.get('tipoCliente'):
                cliente.TipoCliente = str(request.POST.get('tipoCliente'))
            if request.POST.get('enderecoCliente'):
                if cliente.Endereco:
                    cliente.Endereco = setEndereco(cliente.Endereco, request, 'Cliente')
                else:
                    newEndereco = Endereco()
                    cliente.Endereco = setEndereco(newEndereco, request, 'Cliente')

            cliente.save()

            if cliente.Email and not existCliente:
                msg = MIMEMultipart()

                # setup the parameters of the message
                msg['From'] = settings.EMAIL_EMAIL_CLIENTE
                msg['To'] = cliente.Email
                msg['Subject'] = "Você agora é um de nossos clientes"

                mensagem = "Nossos vendedores vão te atender o mais rápido possível. Nossa missão é realizar o seu sonho do automóvel próprio."
                # create server
                msg.attach(MIMEText(mensagem, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com: 587')
                
                server.starttls()
                
                # Login Credentials for sending the mail
                server.login(settings.EMAIL_EMAIL_CLIENTE, settings.PASSWORD_EMAIL_CLIENTE)
                
                
                # send the message via the server.
                server.sendmail(settings.EMAIL_EMAIL_CLIENTE, cliente.Email, msg.as_string())
                
                server.quit()

            return JsonResponse({'msg': 'Cliente cadastrado com sucesso!'}, status=200)

        except Exception as e:
            raise exceptions.ParseError({'msg': 'Erro ao processar o request', 'ex': str(e)})

    def initial(self, request, *args, **kwargs):
        super(cadastrar_cliente_rest, self).initial(request, *args, **kwargs)
