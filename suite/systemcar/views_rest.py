from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.decorators import api_view, permission_classes

@permission_classes((IsAuthenticated,))
class cadastrar_colaborador(APIView):
    """
    Função responsável por cadastrar um colaborador no sistema
    """
    def get(self, request):
        raise exceptions.MethodNotAllowed()

    def post(self, request, *args, **kwargs):
        try:
            usuario = request.user

        except Exception as e:
            raise exceptions.ParseError({'msg': 'Erro ao processar o request', 'ex': str(e)})

    def initial(self, request, *args, **kwargs):
        super(cadastrar_colaborador, self).initial(request, *args, **kwargs)