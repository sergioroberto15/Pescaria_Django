import django_filters
from django_filters import CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    note = CharFilter(field_name='nome', lookup_expr='icontains')
    class Meta:
        model = Pescado
        fields = '__all__'
        exclude = ['nome']

class UsuarioFilter(django_filters.FilterSet):
    note = CharFilter(field_name='nome', lookup_expr='icontains')
    note1 = CharFilter(field_name='sobrenome', lookup_expr='icontains')


    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['user', 'nome', 'sobrenome', 'telefone', 'cpf','endereco']

class PescariaFilter(django_filters.FilterSet):

    class Meta:
        model = Pescaria
        fields = '__all__'
