from django.shortcuts import render

def dashboard(request):
    context = {'url': 'dashboard'}
    return render(request, 'dashboard.html', context)

def configuracoes(request):
    context = {}
    return render(request, 'configuracoes.html', context)

def automoveis_destaque(request):
    context = {}
    return render(request, 'automoveis_destaque.html', context)

def cadastrar_colaborador(request):
    context = {}
    return render(request, 'cadastrar_colaborador.html', context)

def listar_colaboradores(request):
    context = {}
    return render(request, 'listar_colaboradores.html', context)

def cadastrar_cliente(request):
    context = {}
    return render(request, 'cadastrar_cliente.html', context)

def listar_clientes(request):
    context = {}
    return render(request, 'listar_clientes.html', context)

def cadastrar_automovel(request):
    context = {}
    return render(request, 'cadastrar_automovel.html', context)

def listar_automoveis(request):
    context = {}
    return render(request, 'listar_automoveis.html', context)

def cadastrar_contrato(request):
    context = {}
    return render(request, 'cadastrar_contrato.html', context)

def listar_contratos(request):
    context = {}
    return render(request, 'listar_contratos.html', context)

def cadastrar_atendimento(request):
    context = {}
    return render(request, 'cadastrar_atendimento.html', context)

def listar_atendimentos(request):
    context = {}
    return render(request, 'listar_atendimentos.html', context)

def contatos_solicitados(request):
    context = {}
    return render(request, 'contatos_solicitados.html', context)

def leads_solicitadas(request):
    context = {}
    return render(request, 'leads_solicitadas.html', context)