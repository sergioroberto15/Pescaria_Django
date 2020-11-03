from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class PescadoForm(ModelForm):
    class Meta:
        model = Pescado
        fields = '__all__'

class PescariaForm(ModelForm):
    class Meta:
        model = Pescaria
        fields = '__all__'

class CriarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']