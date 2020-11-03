"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('usuario/<str:pk>/', usuario_view, name="usuario"),
    path('pescado/', pescado_view, name="pescado"),
    path('pescaria/', pescaria_view, name="pescaria"),
    path('criarusuario/', criar_usuario, name="criar_usuario"),
    path('atualizarusuario/<str:pk>/', atualizar_usuario, name="atualizar_usuario"),
    path('criarpescado/', criar_pescado, name="criar_pescado"),
    path('atualizarpescado/<str:pk>/', atualizar_pescado, name="atualizar_pescado"),
    path('deletarusuario/<str:pk>/', deletar_usuario, name="deletar_usuario"),
    path('deletarpescado/<str:pk>/', deletar_pescado, name="deletar_pescado"),
    path('criarpescaria/', criar_pescaria, name="criar_pescaria"),
    path('atualizarpescaria/<str:pk>/', atualizar_pescaria, name="atualizar_pescaria"),
    path('deletarpescaria/<str:pk>/', deletar_pescaria, name="deletar_pescaria"),
    path('rankingpeso/', ranking_peso, name="ranking_peso"),
    path('rankingtamanho/', ranking_tamanho, name="ranking_tamanho"),
    path('criarconta/', criar_conta, name="criar_conta"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUsuario, name="logout"),
]
