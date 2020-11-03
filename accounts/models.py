from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    cpf = models.CharField(max_length=11, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome

class Pescaria(models.Model):
    organizador = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    dia = models.CharField(max_length=10)
    hora = models.CharField(max_length=10, blank=True, null=True)
    amigos = models.CharField(max_length=50, blank=True, null=True)
    localizacao = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "esta pescaria"


class Pescado(models.Model):
    nome = models.CharField(max_length=30, null=True)
    massa = models.DecimalField(max_digits=5, decimal_places=2 , null=True)
    tamanho = models.IntegerField(null=True)
    #imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    quemPescou = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome