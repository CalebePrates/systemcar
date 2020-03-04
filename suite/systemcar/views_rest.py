from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes

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
                if request.POST.get('usuarioColaborador') and request.POST.get('senhaColaborador'):
                    usuario = UserManager.objects.create_user(username=str(request.POST.get('usuarioColaborador')),password=str(request.POST.get('senhaColaborador')))
                    usuario.save()
                    colaborador = Colaborador()
                    colaborador.Usuario = usuario
                    colaborador.CriadoPor = request.user
                else:
                    return JsonResponse({'msg': 'Não existe um usuário com as informações passadas ou não foi passado o usuario e senha para a função.'}, status=400)

            if request.POST.get('nomeColaborador'):
                colaborador.Nome = str(request.POST.get('nomeColaborador'))
            if request.POST.get('emailColaborador'):
                colaborador.Email = str(request.POST.get('emailColaborador'))
            if request.POST.get('telefoneColaborador'):
                colaborador.Telefone = str(request.POST.get('telefoneColaborador'))
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

            return JsonResponse({'msg': 'Colaborador cadastrado com sucesso!'}, status=200)

        except Exception as e:
            raise exceptions.ParseError({'msg': 'Erro ao processar o request', 'ex': str(e)})

    def initial(self, request, *args, **kwargs):
        super(cadastrar_colaborador_rest, self).initial(request, *args, **kwargs)
