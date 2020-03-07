from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .lista_opcoes import *
from .models import *
from django.shortcuts import get_object_or_404

# Funções que montam o context e renderiza a página
@login_required
def dashboard(request):
    context = {'url': 'dashboard'}
    return render(request, 'dashboard.html', context)

@login_required
def configuracoes(request):
    context = {}
    return render(request, 'configuracoes.html', context)

@login_required
def automoveis_destaque(request):
    context = {}
    return render(request, 'automoveis_destaque.html', context)

@login_required
def cadastrar_colaborador(request, pk=None):
    situacaoEmpresa = dict((v, k) for k, v in SITUACAO_NA_EMPRESA)
    tiposColaborador = dict((v, k) for k, v in OPCOES_COLABORADOR)

    context = {
        'situacaoEmpresa': situacaoEmpresa,
        'tiposColaborador': tiposColaborador
    }
    return render(request, 'cadastrar_colaborador.html', context)

@login_required
def listar_colaboradores(request, status_cadastro=None):
    """
    Função que renderiza a listagem de colaboradores.
    details:
        -status_cadastro = 0 (sucesso no cadastro)
        -status_cadastro = 1 (erro interno no cadastro de colaborador)
    """
    
    colaboradores = Colaborador.objects.all().order_by('-id')

    context = {
        "colaboradores": colaboradores,
        "status_cadastro": status_cadastro
    }
    
    return render(request, 'listar_colaboradores.html', context)

@login_required
def cadastrar_cliente(request):
    context = {}
    return render(request, 'cadastrar_cliente.html', context)

@login_required
def listar_clientes(request):
    context = {}
    return render(request, 'listar_clientes.html', context)

@login_required
def cadastrar_automovel(request):
    context = {}
    return render(request, 'cadastrar_automovel.html', context)

@login_required
def listar_automoveis(request):
    context = {}
    return render(request, 'listar_automoveis.html', context)

@login_required
def cadastrar_contrato(request):
    context = {}
    return render(request, 'cadastrar_contrato.html', context)

@login_required
def listar_contratos(request):
    context = {}
    return render(request, 'listar_contratos.html', context)

@login_required
def cadastrar_atendimento(request):
    context = {}
    return render(request, 'cadastrar_atendimento.html', context)

@login_required
def listar_atendimentos(request):
    context = {}
    return render(request, 'listar_atendimentos.html', context)

@login_required
def contatos_solicitados(request):
    context = {}
    return render(request, 'contatos_solicitados.html', context)

@login_required
def leads_solicitadas(request):
    context = {}
    return render(request, 'leads_solicitadas.html', context)
# Funções que montam o context e renderiza a página / END

# Funções de edição / BEGIN
def editar_colaborador(request, pk=None):
    situacaoEmpresa = dict((v, k) for k, v in SITUACAO_NA_EMPRESA)
    tiposColaborador = dict((v, k) for k, v in OPCOES_COLABORADOR)
    colaborador = None
    if pk:
        colaborador = get_object_or_404(Colaborador, pk=pk)
    
    context = {
        'situacaoEmpresa': situacaoEmpresa,
        'tiposColaborador': tiposColaborador,
        'colaborador': colaborador
    }
    return render(request, 'cadastrar_colaborador.html', context)
# Funções de edição / END

@login_required
def setEndereco(newEndereco, request, sufixo = ''):
   if request.POST.get('cep' + sufixo):
       newEndereco.CEP = int(str(request.POST.get('cep' + sufixo)).replace('-', ''))
       if request.POST.get('endereco' + sufixo):
           newEndereco.Logradouro = str(request.POST.get('endereco' + sufixo))
       else:
           newEndereco.Logradouro = str('')
       newBairro = Bairro()
       newEndereco.Bairro = setBairro(request, newBairro, sufixo)
   else:
       newEndereco.CEP = str(0)
 
   if request.POST.get('numeroEndereco' + sufixo):
       newEndereco.Numero = str(request.POST.get('numeroEndereco' + sufixo))
   else:
       newEndereco.Numero = str(0)
 
   if request.POST.get('complemento' + sufixo):
       newEndereco.Complemento = str(request.POST.get('complemento' + sufixo))
   else:
       newEndereco.Complemento = str('')
 
   if request.POST.get('latitude_rural') and request.POST.get('longitude_rural'):
       newEndereco.Latitude = str(request.POST.get('latitude_rural')).replace(',','.')
       newEndereco.Longitude = str(request.POST.get('longitude_rural')).replace(',','.')
       if request.POST.get('endereco' + sufixo):
           newEndereco.Logradouro = str(request.POST.get('endereco' + sufixo))
           newBairro = Bairro()
           newEndereco.Bairro = setBairro(request, newBairro, sufixo)
       else:
           newEndereco.Logradouro = str('')
   else:
       mapsAPI = Integrador.objects.filter(Nome='Google Maps API (JS)').first()
       endereco_bairro_cidade = str(newEndereco.Logradouro) + ' ' + str(newEndereco.Numero) + ' ' + str(newEndereco.Bairro) + ' ' + str(newEndereco.Bairro.Cidade)
       GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + endereco_bairro_cidade + '&key=' + mapsAPI.Token
       response = requests.get(GOOGLE_MAPS_API_URL)
 
       resp_json_payload = response.json()
 
       if resp_json_payload['results']:
           newEndereco.Latitude = resp_json_payload['results'][0]['geometry']['location']['lat']
           newEndereco.Longitude = resp_json_payload['results'][0]['geometry']['location']['lng']
   newEndereco.save()
 
   return newEndereco
 
def setBairro(request, newBairro, sufixo):
   newCidade = Cidade()
   newCidade = setCidade(request, newCidade, sufixo)
 
   bairro = Bairro.objects.filter(Nome__unaccent__iexact=(str(request.POST.get('bairro' + sufixo))), Cidade__in=Cidade.objects.filter(id=int(newCidade.id))).first()
   if bairro:
       return bairro
   else:
       if request.POST.get('bairro' + sufixo):
           newBairro.Nome = (str(request.POST.get('bairro' + sufixo)))
       else:
           newBairro.Nome = 'Não identificado'
 
       newBairro.Cidade = newCidade
       newBairro.save()
 
   return newBairro
 
def setCidade(request, newCidade, sufixo):
   newEstado = Estado()
   newEstado = setEstado(request, newEstado, sufixo)
 
   cidade = Cidade.objects.filter(Nome__unaccent__iexact=(str(request.POST.get('cidade' + sufixo))), Estado__in=Estado.objects.filter(id=int(newEstado.id))).first()
   if cidade:
       return cidade
   else:
       if request.POST.get('cidade' + sufixo):
           newCidade.Nome = (str(request.POST.get('cidade' + sufixo)))
           newCidade.NomeNormalizado = unidecode.unidecode(str(request.POST.get('cidade' + sufixo)))
       else:
           newCidade.Nome = 'Não identificado'
 
       newCidade.Estado = newEstado
       newCidade.save()
 
   return newCidade
 
def setEstado(request, newEstado, sufixo):
   estado = Estado.objects.filter(Sigla__unaccent__iexact=(str(request.POST.get('siglaEstado' + sufixo)))).first()
 
   if estado:
       return estado
   else:
       if request.POST.get('estado' + sufixo):
           newEstado.Estado = (str(request.POST.get('estado' + sufixo)))
       elif request.POST.get('siglaEstado' + sufixo):
           newEstado.Sigla = (str(request.POST.get('siglaEstado' + sufixo)))
           newEstado.Estado = (str(request.POST.get('siglaEstado' + sufixo)))
       else:
           newEstado.Sigla = 'Não identificado'
           newEstado.Estado = 'Não identificado'
 
       newEstado.save()
 
   return newEstado