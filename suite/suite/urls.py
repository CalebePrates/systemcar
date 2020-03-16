from django.contrib import admin
from django.urls import path
from systemcar import views, views_admin, views_rest
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers

#SERIALIZAERS ROUTERS
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),

    path('admin-systemcar/', admin.site.urls),
    path('admin/', views_admin.dashboard, name='dashboard'),

    path('admin/meu_perfil/', views_admin.meu_perfil, name='meu_perfil'),
    
    # URLS DO MENU AVANÇADO
    path('admin/configuracoes/', views_admin.configuracoes, name='configuracoes'),
    path('admin/automoveis_destaque/', views_admin.automoveis_destaque, name='automoveis_destaque'),
    # URLS DO MENU AVANÇADO / END

    # URLS DO MENU COLABORADOR
    path('admin/cadastrar_colaborador/', views_admin.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('admin/editar_colaborador/<int:pk>', views_admin.editar_colaborador, name='editar_colaborador'),
    path('admin/listar_colaboradores/<int:status_cadastro>', views_admin.listar_colaboradores, name='listar_colaboradores'),
    path('admin/listar_colaboradores/', views_admin.listar_colaboradores, name='listar_colaboradores'),
    # URLS DO MENU COLABORADOR / END
    
    # URLS DO MENU CLIENTE
    path('admin/cadastrar_cliente/', views_admin.cadastrar_cliente, name='cadastrar_cliente'),
    path('admin/editar_cliente/<int:pk>', views_admin.editar_cliente, name='editar_cliente'),
    path('admin/listar_clientes/<int:status_cadastro>', views_admin.listar_clientes, name='listar_clientes'),
    path('admin/listar_clientes/', views_admin.listar_clientes, name='listar_clientes'),
    # URLS DO MENU CLIENTE / END

    # URLS DO MENU AUTOMOVEL
    path('admin/cadastrar_automovel/', views_admin.cadastrar_automovel, name='cadastrar_automovel'),
    path('admin/listar_automoveis/', views_admin.listar_automoveis, name='listar_automoveis'),
    # URLS DO MENU AUTOMOVEL / END

    # URLS DO MENU CONTRATO
    path('admin/cadastrar_contrato/', views_admin.cadastrar_contrato, name='cadastrar_contrato'),
    path('admin/listar_contratos/', views_admin.listar_contratos, name='listar_contratos'),
    # URLS DO MENU CONTRATO / END
    
    # URLS DO MENU ATENDIMENTO
    path('admin/cadastrar_atendimento/', views_admin.cadastrar_atendimento, name='cadastrar_atendimento'),
    path('admin/listar_atendimentos/', views_admin.listar_atendimentos, name='listar_atendimentos'),
    # URLS DO MENU ATENDIMENTO / END

    path('admin/contatos_solicitados/', views_admin.contatos_solicitados, name='contatos_solicitados'),
    path('admin/leads_solicitadas/', views_admin.leads_solicitadas, name='leads_solicitadas'),

    # Funções REST
    path('rest/cadastrar_colaborador_rest/', views_rest.cadastrar_colaborador_rest.as_view(), name='cadastrar_colaborador_rest'),
    path('rest/cadastrar_cliente_rest/', views_rest.cadastrar_cliente_rest.as_view(), name='cadastrar_cliente_rest'),
    # Funções REST / END
]