from django.http import HttpResponse
from django.shortcuts import render


# Página principal (home general del sistema)
def login(request):
    return render(request, 'usuarios/login.html')

def home(request):
    return render(request, 'usuarios/home_principal.html')


def home_administrador(request):
    return render(request, 'usuarios/home_administrador.html')

def home_usuario(request):
    return render(request, 'usuarios/home_usuario.html')

def registro_usuario(request):
    return render(request, 'usuarios/registro_usuario.html')

def gestionar_usuarios(request):
    return render(request, 'gestionar_usuarios.html')

def registrar_funcionario(request):
    return render(request, 'registrar_funcionario.html')

def gestionar_funcionarios(request):
    return render(request, 'gestionar_funcionarios.html')

def sobre_mi(request):
    return render(request, 'usuarios/sobre_mi.html')

def manual(request):
    return render(request, 'manual.html')

def olvido_contrasena(request):
    return render(request, "usuarios/olvido_contrasena.html")

def editar_perfil(request):
    return render(request, "usuarios/editar_perfil.html")

def cambiar_contraseña(request):
    return render(request, "usuarios/cambiar_contraseña.html")

def terminos_condiciones(request):
    return render(request, 'usuarios/terminos_condiciones.html')