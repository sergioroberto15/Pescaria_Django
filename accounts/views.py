from django.shortcuts import render, redirect
from .models import *
from .forms import UsuarioForm, PescadoForm, PescariaForm, CriarUsuarioForm
from .filters import OrderFilter, UsuarioFilter, PescariaFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# Registro, Login e Logout

def criar_conta(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CriarUsuarioForm()

        if request.method == 'POST':
            form = CriarUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Conta criada com sucesso')
                return redirect('login')

        context = {'form': form}

        return render(request, "criar_conta.html", context)

def loginPage (request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuário OU senha incorretos.')

        context = {}

        return render(request, "login.html", context)

def logoutUsuario (request):
    logout(request)
    return redirect('login')

# Páginas

@login_required(login_url='login')
def home_view(request):
    usuario_view = Usuario.objects.all()
    pescado_view = Pescado.objects.all()
    pescaria_view = Pescaria.objects.all()

    quantia_pescada = pescado_view.count
    total_pescadores = usuario_view.count
    total_pescaria = pescaria_view.count

    myFilter = UsuarioFilter(request.GET, queryset=usuario_view)
    usuario_view = myFilter.qs

    context = {'usuarios': usuario_view, 'pescados': pescado_view, 'quantia_pescada': quantia_pescada,
               'total_pescadores': total_pescadores, 'total_pescaria': total_pescaria, 'myFilter': myFilter}

    return render(request, "home.html", context)

@login_required(login_url='login')
def usuario_view(request, pk):

    usuario = Usuario.objects.get(id=pk)
    pescado = usuario.pescado_set.all()
    pescarias = usuario.pescaria_set.all()


    context = {'usuario': usuario, 'pescados': pescado, 'pescarias': pescarias}

    return render(request, "usuario.html", context)

@login_required(login_url='login')
def pescado_view(request):
    pescado_view = Pescado.objects.all()
    myFilter = OrderFilter(request.GET, queryset=pescado_view)
    pescado_view = myFilter.qs


    return render(request, "pescado.html", {'pescados': pescado_view, 'myFilter': myFilter})

@login_required(login_url='login')
def pescaria_view(request):
    pescaria_view = Pescaria.objects.all()

    myFilter = PescariaFilter(request.GET, queryset=pescaria_view)
    pescaria_view = myFilter.qs

    return render(request, "pescaria.html", {'pescarias': pescaria_view, 'myFilter': myFilter})

# Criar, Atualizar e Deletar Usuários(Pescadores)

@login_required(login_url='login')
def criar_usuario(request):

    form = UsuarioForm
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, "usuario_formulario.html", context)

@login_required(login_url='login')
def atualizar_usuario(request, pk):

    usuario = Usuario.objects.get(id=pk)
    form = UsuarioForm(instance=usuario)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, "usuario_formulario.html", context)

@login_required(login_url='login')
def deletar_usuario(request, pk):

    usuario = Usuario.objects.get(id=pk)

    if request.method == 'POST':
        usuario.delete()
        return redirect('/')

    context = {'item': usuario}

    return render(request, "delete.html", context)

# Criar, Atualizar e Deletar Pescado

@login_required(login_url='login')
def criar_pescado(request):

    form = PescadoForm
    if request.method == 'POST':
        form = PescadoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, "pescado_formulario.html", context)

@login_required(login_url='login')
def atualizar_pescado(request, pk):

    pescado = Pescado.objects.get(id=pk)
    form = PescadoForm(instance=pescado)

    if request.method == 'POST':
        form = PescadoForm(request.POST, instance=pescado)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, "pescado_formulario.html", context)

@login_required(login_url='login')
def deletar_pescado(request, pk):

    pescado = Pescado.objects.get(id=pk)

    if request.method == 'POST':
        pescado.delete()
        return redirect('/')

    context = {'item': pescado}

    return render(request, "delete.html", context)

# Criar, Atualizar e Deletar Pescaria

@login_required(login_url='login')
def criar_pescaria(request):

    form = PescariaForm
    if request.method == 'POST':
        form = PescariaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, "pescaria_formulario.html", context)

@login_required(login_url='login')
def atualizar_pescaria(request, pk):

    pescaria = Pescaria.objects.get(id=pk)
    form = PescariaForm(instance=pescaria)

    if request.method == 'POST':
        form = PescariaForm(request.POST, instance=pescaria)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, "pescaria_formulario.html", context)

@login_required(login_url='login')
def deletar_pescaria(request, pk):

    pescaria = Pescaria.objects.get(id=pk)

    if request.method == 'POST':
        pescaria.delete()
        return redirect('/')

    context = {'item': pescaria}

    return render(request, "delete.html", context)

# Rankings de peso e tamanho

@login_required(login_url='login')
def ranking_peso(request):
    pescado_view = Pescado.objects.order_by('-massa')

    context = {'pescados': pescado_view}

    return render(request, "ranking_peso.html", context)

@login_required(login_url='login')
def ranking_tamanho(request):
    pescado_view = Pescado.objects.order_by('-tamanho')

    context = {'pescados': pescado_view}

    return render(request, "ranking_tamanho.html", context)